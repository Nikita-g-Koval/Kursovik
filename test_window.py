from tkinter import *
from tkinter import messagebox
from validation import Validation
from user import User
from questionsStrorage import QuestionsStorage
from diagnosesStorage import DiagnosesStorage


font_header = ('Arial', 15)
font_entry = ('Arial', 12)
lable_font = ('Arial', 11)
base_padding = {'padx': 10, 'pady': 8}
header_padding = {'padx': 10, 'pady': 12}


class TestWindow:
    def __init__(self, user: User, questions_storage: QuestionsStorage):
        self.user = user
        self.questions_storage = questions_storage
        self.test_window = Tk()
        self.test_window.title("Тест")
        self.test_window.geometry('800x300')
        self.test_window.resizable(False, False)

        self.diagnoses = DiagnosesStorage()
        self.qs = QuestionsStorage()
        self.questions = self.qs.shuffle()
        self.questionId = 0

        self.test_label = Label(self.test_window, text="Вопрос №{0}:".format(self.questionId + 1)
                                                       + self.questions[self.questionId].text, font=font_entry,
                                justify=CENTER, **header_padding)
        self.test_label.pack()

        self.userAnswer_entry = Entry(self.test_window, bg='#fff', fg='#444', font=font_entry)
        self.userAnswer_entry.pack()

        self.acceptAnswer_btn = Button(self.test_window, text='Ответить', command=self.accept_answer_btn_clicked)
        self.acceptAnswer_btn.pack(**base_padding)

    def accept_answer_btn_clicked(self):
        input_answer = self.userAnswer_entry.get()
        if not Validation.ValidateAnswer(input_answer):
            messagebox.showwarning(
                title="Предупреждение",
                message="Введены некорректные данные! Введите целочисленное число в разумных пределах.")
            return
        if int(input_answer) == self.questions[self.questionId].answer:
            self.user.rightAnswersCount += 1
        if self.questionId >= len(self.questions)-1:
            diagnosis = self.diagnoses.calculate_diagnose(len(self.questions), self.user.rightAnswersCount)
            messagebox.showinfo(title="Тест завершён", message="{0}, ваш диагноз: {1}".format(self.user.name,
                                                                                              diagnosis.grade))
            return
        self.userAnswer_entry.delete(0, END)
        self.questionId += 1
        self.show_next_question()

    def show_next_question(self):
        self.test_label.config(text="Вопрос №{0}:".format(self.questionId+1) + self.questions[self.questionId].text)

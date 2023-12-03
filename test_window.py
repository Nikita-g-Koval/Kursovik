from tkinter import *
from tkinter import ttk
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
position = {"padx":6, "pady":6, "anchor":NW}


class TestWindow:
    def __init__(self, user: User, questions_storage: QuestionsStorage):
        self.user = user
        self.questions_storage = questions_storage
        self.test_window = Tk()
        self.test_window.title("Тест")
        self.test_window.geometry('800x300')
        self.test_window.resizable(True, True)

        self.diagnoses = DiagnosesStorage()
        self.qs = QuestionsStorage()
        self.questions = self.qs.shuffle()
        self.questionId = 0

        self.test_label = Label(self.test_window, text="Вопрос №{0}:".format(self.questionId + 1)
                                                       + self.questions[self.questionId].text, font=font_entry,
                                justify=CENTER, **header_padding)
        self.test_label.pack()

        answers = self.questions[self.questionId].answers
        self.selected_answer = BooleanVar()
        self.radiobuttons = []
        for answer in answers:
            answer_btn = ttk.Radiobutton(self.test_window, text=answer.text, value=answer.is_correct,
                                         variable=self.selected_answer)
            answer_btn.pack(**base_padding)
            self.radiobuttons.append(answer_btn)

        self.acceptAnswer_btn = Button(self.test_window, text='Ответить', command=self.accept_answer_btn_clicked)
        self.acceptAnswer_btn.pack(**base_padding)

    def accept_answer_btn_clicked(self):
        if self.selected_answer:
            self.user.rightAnswersCount += 1
        if self.questionId >= len(self.questions)-1:
            diagnosis = self.diagnoses.calculate_diagnose(len(self.questions), self.user.rightAnswersCount)
            messagebox.showinfo(title="Тест завершён", message="{0}, ваш диагноз: {1}".format(self.user.name,
                                                                                              diagnosis.grade))
            return
        self.questionId += 1
        self.show_next_question()

    def show_next_question(self):
        self.test_label.config(text="Вопрос №{0}:".format(self.questionId+1) + self.questions[self.questionId].text)
        for btn in self.radiobuttons:
            btn.destroy()

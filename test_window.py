from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from answer import Answer
from user import User
from questionsStrorage import QuestionsStorage
from diagnosesStorage import DiagnosesStorage


font_header = ('Arial', 15)
font_entry = ('Arial', 12)
lable_font = ('Arial', 11)
base_padding = {'padx': 10, 'pady': 8}
header_padding = {'padx': 10, 'pady': 12}
position = {'anchor': S}


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

        questions = self.qs.questions
        self.questions = self.qs.shuffle(questions)
        self.questionId = 0

        answers = self.questions[self.questionId].answers
        self.answers = self.qs.shuffle(answers)

        self.test_label = Label(self.test_window, text="Вопрос №{0}:".format(self.questionId + 1)
                                                       + self.questions[self.questionId].text, font=font_entry,
                                justify=CENTER, **header_padding)
        self.test_label.pack()

        self.selected_id = IntVar(self.test_window)

        self.radio_buttons = []

        self.init_radiobuttons()

        self.acceptAnswer_btn = Button(self.test_window, text='Ответить', command=self.accept_answer_btn_clicked)
        self.acceptAnswer_btn.pack(pady=10, side=BOTTOM)

    def get_answer(self):
        answer: Answer = self.answers[self.selected_id.get()]
        return answer

    def accept_answer_btn_clicked(self):
        if self.get_answer().is_correct:
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
        self.clear_radiobuttons()
        self.init_radiobuttons()

    def init_radiobuttons(self):
        answers = self.questions[self.questionId].answers
        self.answers = self.qs.shuffle(answers)

        self.selected_id.set(0)

        for i in range(len(self.answers)):
            answer_btn = ttk.Radiobutton(self.test_window, text=self.answers[i].text, value=i,
                                         variable=self.selected_id)
            answer_btn.pack(**base_padding)
            self.radio_buttons.append(answer_btn)

    def clear_radiobuttons(self):
        for btn in self.radio_buttons:
            btn.destroy()
        self.radio_buttons.clear()

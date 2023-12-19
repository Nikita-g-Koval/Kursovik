from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
from question_type import QuestionType
from test_result import TestResult
from answer import Answer
from user import User
from fileProvider import FileProvider
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
        self.rightAnswersCount = 0
        self.test_result = None

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

        self.shuffled_answers = self.qs.shuffle(self.current_answers)

        self.test_label = Label(self.test_window, font=font_entry,
                                justify=CENTER, **header_padding)
        self.test_label.pack()

        self.selected_id = IntVar(self.test_window)
        self.answer_entry = Entry(self.test_window)
        self.radio_buttons = []
        self.check_buttons = []
        self.selected_buttons = []

        self.save_results_btn = Button(self.test_window, text='Сохранить результаты',
                                       command=self.save_results_btn_click)
        self.save_results_btn.pack(pady=10, side=BOTTOM)

        self.acceptAnswer_btn = Button(self.test_window, text='Ответить', command=self.accept_answer_btn_clicked)
        self.acceptAnswer_btn.pack(side=BOTTOM)

        self.show_next_question()

    def save_results_btn_click(self):
        if self.test_result is None:
            messagebox.showwarning(title="Предупреждение", message="Сначала пройдите тест!")
            return

        FileProvider.save_test_result(self.test_result)
        messagebox.showinfo(title="Сообщение", message="Результаты успешно сохранены.")

    @property
    def current_question(self):
        return self.questions[self.questionId]

    @property
    def current_answers(self):
        return self.current_question.answers

    def show_answers(self):
        self.clear_answers()

        match self.current_question.get_type:
            case QuestionType.base:
                self.answer_entry = Entry(self.test_window, bg='#fff', fg='#444', font=font_entry)
                self.answer_entry.pack(**base_padding)
            case QuestionType.radio_button:
                self.init_radiobuttons()
            case QuestionType.check_button:
                self.init_checkbuttons()

    def get_answer_from_radiobutton(self):
        answer: Answer = self.shuffled_answers[self.selected_id.get()]
        return answer

    def accept_answer_btn_clicked(self):
        match self.current_question.get_type:
            case QuestionType.base:
                if self.answer_entry.get() == self.current_answers[0].text:
                    self.rightAnswersCount += 1
            case QuestionType.radio_button:
                if self.get_answer_from_radiobutton().is_correct:
                    self.rightAnswersCount += 1
            case QuestionType.check_button:
                attempts = 0
                successful_attempts = 0
                for btn in self.selected_buttons:
                    if btn.get() > len(self.shuffled_answers):
                        continue
                    attempts += 1

                    if self.shuffled_answers[btn.get()].is_correct:
                        successful_attempts += 1

                successful_percentage = successful_attempts/attempts * 100

                if successful_percentage > 50:
                    self.rightAnswersCount += 1

        if self.questionId >= len(self.questions)-1:
            diagnosis = self.diagnoses.calculate_diagnose(len(self.questions), self.rightAnswersCount)
            self.test_result = TestResult(self.user, self.rightAnswersCount, diagnosis, datetime.now())
            self.acceptAnswer_btn.config(state=DISABLED)
            messagebox.showinfo(title="Тест завершён", message="{0}, ваш диагноз: {1}".format(self.user.name,
                                                                                              diagnosis.grade))
            return

        self.questionId += 1
        self.show_next_question()

    def show_next_question(self):
        self.test_label.config(text="Вопрос №{0}:".format(self.questionId+1) + self.current_question.text)
        self.show_answers()

    def init_radiobuttons(self):
        self.shuffled_answers = self.qs.shuffle(self.current_answers)

        self.selected_id.set(0)

        for i in range(len(self.shuffled_answers)):
            answer_btn = ttk.Radiobutton(self.test_window, text=self.shuffled_answers[i].text, value=i,
                                         variable=self.selected_id)
            answer_btn.pack(**base_padding)
            self.radio_buttons.append(answer_btn)

    def init_checkbuttons(self):
        self.shuffled_answers = self.qs.shuffle(self.current_answers)

        for i in range(len(self.shuffled_answers)):
            selected_id = IntVar(self.test_window)
            selected_id.set(len(self.shuffled_answers) + 1)
            self.selected_buttons.append(selected_id)

            answer_btn = ttk.Checkbutton(self.test_window, text=self.shuffled_answers[i].text,
                                         offvalue=len(self.shuffled_answers) + 1,
                                         onvalue=i,
                                         variable=selected_id)
            answer_btn.pack(**base_padding)
            self.check_buttons.append(answer_btn)

    def clear_answers(self):
        self.answer_entry.destroy()
        for btn in self.radio_buttons:
            btn.destroy()

        for btn in self.check_buttons:
            btn.destroy()

        self.radio_buttons.clear()
        self.check_buttons.clear()
        self.selected_buttons.clear()

from tkinter import *
from tkinter import messagebox
from questionsStrorage import QuestionsStorage
from validation import Validation
from fileProvider import FileProvider
from question import Question
from answer import Answer


class AddBaseQuestionWindow:
    def __init__(self, questions_storage: QuestionsStorage):
        self.questions_storage = questions_storage
        self.addBaseQuestion_window = Tk()
        self.addBaseQuestion_window.title('Добавление вопроса')
        self.addBaseQuestion_window.geometry('870x100')
        self.addBaseQuestion_window.resizable(False, True)

        Label(self.addBaseQuestion_window, text="Текст вопроса:").grid(row=0, column=0)
        self.questionText_entry = Entry(self.addBaseQuestion_window, width=120)
        self.questionText_entry.grid(row=0, column=1)

        Label(self.addBaseQuestion_window, text="Ответ на вопрос:").grid(row=1, column=0)
        self.answer_entry = Entry(self.addBaseQuestion_window, width=120)
        self.answer_entry.grid(row=1, column=1)

        self.add_question_btn = Button(self.addBaseQuestion_window, text="Добавить вопрос",
                                       command=self.add_answer_btn_click)
        self.add_question_btn.grid(row=2, column=0, sticky=EW)

        self.save_changes_btn = Button(self.addBaseQuestion_window, text="Сохранить изменения",
                                       command=self.save_changes_btn_click)
        self.save_changes_btn.grid(row=3, column=0, sticky=EW)

    def add_answer_btn_click(self):
        input_question = self.questionText_entry.get()
        input_answer = self.answer_entry.get()

        if not Validation.ValidateQuestion(input_question):
            messagebox.showwarning(title="Предупреждение", message="Длина вопроса должна быть > 0 и < 120.")
            return

        if not Validation.ValidateAnswer(input_answer):
            messagebox.showwarning(title="Предупреждение", message="Не был введён ответ.")
            return

        answers = [Answer(input_answer, True)]
        question = Question(input_question, answers)

        self.questions_storage.add_question(question)
        messagebox.showinfo(title="Оповещение", message="Вопрос успешно добавлен. Сохраните изменения.")

    def save_changes_btn_click(self):
        FileProvider.save_questions(self.questions_storage.questions)
        messagebox.showinfo(title="Оповещение", message="Изменения сохранены.")
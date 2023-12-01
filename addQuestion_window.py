from tkinter import *
from tkinter import messagebox
from questionsStrorage import QuestionsStorage
from validation import Validation
from fileProvider import FileProvider
from question import Question


class AddQuestionWindow:
    def __init__(self, questions_storage: QuestionsStorage):
        self.new_question = None
        self.questions_storage = questions_storage
        self.addQuestion_window = Tk()
        self.addQuestion_window.title('Добавление вопроса')
        self.addQuestion_window.geometry('400x100')
        self.addQuestion_window.resizable(False, False)

        Label(self.addQuestion_window, text="Текст вопроса:", justify=LEFT).grid(row=0, column=0, sticky=W)
        self.questionText_entry = Entry(self.addQuestion_window, width=30)
        self.questionText_entry.grid(row=0, column=1, sticky=EW)

        Label(self.addQuestion_window, text="Ответ на вопрос:", justify=LEFT).grid(row=1, column=0, sticky=W)
        self.answer_entry = Entry(self.addQuestion_window, width=30)
        self.answer_entry.grid(row=1, column=1, sticky=EW)

        self.add_question_btn = Button(self.addQuestion_window, text='Добавить вопрос',
                                       command=self.add_question_btn_click)
        self.add_question_btn.grid(row=2, sticky=W+E)

        self.save_changes_btn = Button(self.addQuestion_window, text='Сохранить изменения',
                                       command=self.save_changes_btn_click)
        self.save_changes_btn.grid(row=3, sticky=W+E)

    def add_question_btn_click(self):
        question_text = self.questionText_entry.get()
        answer = self.answer_entry.get()

        if not Validation.ValidateQuestion(question_text):
            messagebox.showwarning(title="Предупреждение",
                                   message="Введены некорректные данные! Введите текст вопроса.")
            return

        if not Validation.ValidateAnswer(answer):
            messagebox.showwarning(title="Предупреждение",
                                   message="Введены некорректные данные! Введите целочисленный ответ на вопрос.")
            return

        self.new_question = Question(question_text, answer)
        self.questions_storage.add_question(self.new_question)
        messagebox.showinfo(title="Успешно", message="Вопрос добавлен.")

    def save_changes_btn_click(self):
        FileProvider.save_questions(self.questions_storage.questions)
        messagebox.showinfo(title="Успешно", message="Изменения сохранены.")

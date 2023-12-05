from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from typing import List
from questionsStrorage import QuestionsStorage
from validation import Validation
from fileProvider import FileProvider
from question import Question
from answer import Answer


class AddQuestionWindow:
    def __init__(self, questions_storage: QuestionsStorage):
        self.new_question: Question = None
        self.answers: List[Answer] = []
        self.questions_storage = questions_storage
        self.addQuestion_window = Tk()
        self.addQuestion_window.title('Добавление вопроса')
        self.addQuestion_window.geometry('900x200')
        self.addQuestion_window.resizable(False, True)
        self.selected_id = IntVar(self.addQuestion_window)
        self.radio_buttons = []

        Label(self.addQuestion_window, text="Текст вопроса:", justify=LEFT).grid(row=0, column=0, sticky=W)
        self.questionText_entry = Entry(self.addQuestion_window, width=30)
        self.questionText_entry.grid(row=0, column=1, sticky=EW)

        Label(self.addQuestion_window, text="Ответ на вопрос:", justify=LEFT).grid(row=1, column=0, sticky=W)
        self.answer_entry = Entry(self.addQuestion_window, width=30)
        self.answer_entry.grid(row=1, column=1, sticky=EW)

        Label(self.addQuestion_window, text="Ответ правильный? (True/False):").grid(row=1, column=2)
        self.answer_is_correct_entry = Entry(self.addQuestion_window, width=30)
        self.answer_is_correct_entry.grid(row=1, column=3)

        self.addAnswer_btn = Button(self.addQuestion_window, text='Добавить ответ', command=self.add_answer_btn_click)
        self.addAnswer_btn.grid(padx=40, row=1, column=4, sticky=EW)

        self.removeAnswer_btn = Button(self.addQuestion_window, text="Удалить выбранный ответ",
                                       command=self.remove_answer_btn_click)
        self.removeAnswer_btn.grid(padx=40, row=2, column=4, sticky=EW)

        self.add_question_btn = Button(self.addQuestion_window, text='Добавить вопрос',
                                       command=self.add_question_btn_click)
        self.add_question_btn.grid(row=2, sticky=W+E)

        self.save_changes_btn = Button(self.addQuestion_window, text='Сохранить изменения',
                                       command=self.save_changes_btn_click)
        self.save_changes_btn.grid(row=3, sticky=W+E)

    def add_answer_btn_click(self):
        if len(self.answers) >= 6:
            messagebox.showwarning(title="Предупреждение",
                                   message="Максимальное количество ответов 6. Больше добавить нельзя.")
            return
        input_answer = self.answer_entry.get()
        if len(input_answer) == 0:
            messagebox.showwarning(title="Предупреждение", message="Данные не были введены!")
            return

        input_correctness = self.answer_is_correct_entry.get()
        if not (input_correctness.lower() == 'false' or input_correctness.lower() == 'true'):
            messagebox.showwarning(title="Предупреждение", message="Укажите верность ответа True или False")
            return

        answer = Answer(input_answer, input_correctness == 'True')
        self.answers.append(answer)
        self.init_radiobuttons()

    def remove_answer_btn_click(self):
        if len(self.answers) > 0:
            del self.answers[self.selected_id.get()]
            self.init_radiobuttons()

    def add_question_btn_click(self):
        question_text = self.questionText_entry.get()
        answer = self.answer_entry.get()

        if not Validation.ValidateQuestion(question_text):
            messagebox.showwarning(title="Предупреждение",
                                   message="Введены некорректные данные! Введите текст вопроса.")
            return

        if len(self.answers) < 2:
            messagebox.showwarning(title="Предупреждение",
                                   message="Количество вопросов должно быть не менее двух!")
            return

        if not self.had_correct_answer():
            messagebox.showwarning(title="Предупреждение",
                                   message="Хотя бы один вопрос должен быть правильным!")
            return

        self.new_question = Question(question_text, answer)
        self.questions_storage.add_question(self.new_question)
        messagebox.showinfo(title="Успешно", message="Вопрос добавлен.")

    def save_changes_btn_click(self):
        FileProvider.save_questions(self.questions_storage.questions)
        messagebox.showinfo(title="Успешно", message="Изменения сохранены.")

    def init_radiobuttons(self):
        self.clear_radiobuttons()
        for i in range(len(self.answers)):
            answer_btn = ttk.Radiobutton(self.addQuestion_window, text=self.answers[i].text, value=i,
                                         variable=self.selected_id)
            answer_btn.grid(row=i+2, column=3)
            self.radio_buttons.append(answer_btn)

    def clear_radiobuttons(self):
        for btn in self.radio_buttons:
            btn.destroy()
        self.radio_buttons.clear()

    def had_correct_answer(self):
        one_is_correct = False
        for answer in self.answers:
            if answer.is_correct:
                one_is_correct = True
                break

        return one_is_correct

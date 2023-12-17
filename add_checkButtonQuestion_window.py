from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from typing import List
from questionsStrorage import QuestionsStorage
from validation import Validation
from fileProvider import FileProvider
from question import Question
from answer import Answer
from question_checkButton import QuestionRadioButton


class AddCheckButtonQuestion:
    new_question: Question

    def __init__(self, questions_storage: QuestionsStorage):
        self.answers: List[Answer] = []
        self.questions_storage = questions_storage
        self.add_checkButtonQuestion_window = Tk()
        self.add_checkButtonQuestion_window.title('Добавление вопроса с множественным выбором')
        self.add_checkButtonQuestion_window.geometry('900x200')
        self.add_checkButtonQuestion_window.resizable(False, True)
        self.check_buttons = []
        self.selections : List[IntVar] = []

        Label(self.add_checkButtonQuestion_window, text="Текст вопроса:", justify=LEFT).grid(row=0, column=0, sticky=W)
        self.questionText_entry = Entry(self.add_checkButtonQuestion_window, width=30)
        self.questionText_entry.grid(row=0, column=1, sticky=EW)

        Label(self.add_checkButtonQuestion_window, text="Ответ на вопрос:",
              justify=LEFT).grid(row=1, column=0, sticky=W)
        self.answer_entry = Entry(self.add_checkButtonQuestion_window, width=30)
        self.answer_entry.grid(row=1, column=1, sticky=EW)

        Label(self.add_checkButtonQuestion_window, text="Ответ правильный? (True/False):").grid(row=1, column=2)
        self.answer_is_correct_entry = Entry(self.add_checkButtonQuestion_window, width=30)
        self.answer_is_correct_entry.grid(row=1, column=3)

        self.add_answer_btn = Button(self.add_checkButtonQuestion_window, text="Добавить ответ",
                                     command=self.add_answer_btn_click)
        self.add_answer_btn.grid(row=2, column=0)

        self.remove_answer_btn = Button(self.add_checkButtonQuestion_window, text="Удалить ответ",
                                        command=self.remove_answer_btn_click)
        self.remove_answer_btn.grid(row=2, column=1)

        self.add_question_btn = Button(self.add_checkButtonQuestion_window, text="Добавить вопрос",
                                       command=self.add_question_btn_click)
        self.add_question_btn.grid(row=3, column=0)

        self.save_changes_btn = Button(self.add_checkButtonQuestion_window, text="Сохранить изменения",
                                       command=self.save_changes_btn_click)
        self.save_changes_btn.grid(row=4, column=0)

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
        if not (input_correctness.lower() == 't' or input_correctness.lower() == 'f'):
            messagebox.showwarning(title="Предупреждение", message="Укажите верность ответа T/F")
            return

        answer = Answer(input_answer, input_correctness.lower() == 't')
        self.answers.append(answer)
        self.init_checkbuttons()

    def remove_answer_btn_click(self):
        if len(self.answers) > 0:
            selected_answers = []

            for select in self.selections:
                if select.get() > len(self.answers):
                    continue

                selected_answers.append(self.answers[select.get()])

            for answer in selected_answers:
                self.answers.remove(answer)

            self.init_checkbuttons()

    def add_question_btn_click(self):
        question_text = self.questionText_entry.get()

        if not Validation.ValidateQuestion(question_text):
            messagebox.showwarning(title="Предупреждение",
                                   message="Введены некорректные данные! Введите текст вопроса.")
            return

        if len(self.answers) < 2:
            messagebox.showwarning(title="Предупреждение",
                                   message="Количество вопросов должно быть не менее двух!")
            return

        self.new_question = QuestionRadioButton(question_text, self.answers)
        self.questions_storage.add_question(self.new_question)
        messagebox.showinfo(title="Успешно", message="Вопрос добавлен.")

    def save_changes_btn_click(self):
        FileProvider.save_questions(self.questions_storage.questions)
        messagebox.showinfo(title="Успешно", message="Изменения сохранены.")

    def init_checkbuttons(self):
        self.clear_checkbuttons()

        for i in range(len(self.answers)):
            selected_id = IntVar(self.add_checkButtonQuestion_window)
            selected_id.set(len(self.answers) + 1)
            self.selections.append(selected_id)

            answer_btn = ttk.Checkbutton(self.add_checkButtonQuestion_window, text=self.answers[i].text,
                                         offvalue=len(self.answers) + 1,
                                         onvalue=i,
                                         variable=selected_id)
            answer_btn.grid(row=i+2, column=2)
            self.check_buttons.append(answer_btn)

    def clear_checkbuttons(self):
        for btn in self.check_buttons:
            btn.destroy()
        self.check_buttons.clear()
        self.selections.clear()

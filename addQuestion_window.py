from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from typing import List
from questionsStrorage import QuestionsStorage
from validation import Validation
from fileProvider import FileProvider
from question import Question
from answer import Answer
from add_baseQuestion_window import AddBaseQuestionWindow
from add_radioButtonQuestion_window import AddRadioButtonQuestion


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

        self.add_baseQuestion_btn = Button(self.addQuestion_window, text="Добавить базовый вопрос",
                                           command=self.add_base_question_btn_click)
        self.add_baseQuestion_btn.grid(row=2, column=0)

        self.add_radioButtonQuestion_btn = Button(self.addQuestion_window, text="Добавить вопрос с выбором",
                                                  command=self.add_radiobutton_question_btn_click)
        self.add_radioButtonQuestion_btn.grid(row=2, column=1)

    def add_base_question_btn_click(self):
        AddBaseQuestionWindow(self.questions_storage)

    def add_radiobutton_question_btn_click(self):
        AddRadioButtonQuestion(self.questions_storage)

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

        answer = Answer(input_answer, input_correctness.lower() == 'true')
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

        self.new_question = Question(question_text, self.answers)
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
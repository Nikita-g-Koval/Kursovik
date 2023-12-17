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
from add_checkButtonQuestion_window import AddCheckButtonQuestion


class AddQuestionWindow:
    def __init__(self, questions_storage: QuestionsStorage):
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
        self.add_baseQuestion_btn.grid(row=0, column=0)

        self.add_radioButtonQuestion_btn = Button(self.addQuestion_window, text="Добавить вопрос с выбором",
                                                  command=self.add_radiobutton_question_btn_click)
        self.add_radioButtonQuestion_btn.grid(row=1, column=0)

        self.add_checkButtonQuestion_btn = Button(self.addQuestion_window,
                                                  text="Добавить вопрос с множественным выбором",
                                                  command=self.add_checkbutton_question_btn_click)
        self.add_checkButtonQuestion_btn.grid(row=2, column=0)

    def add_base_question_btn_click(self):
        AddBaseQuestionWindow(self.questions_storage)

    def add_radiobutton_question_btn_click(self):
        AddRadioButtonQuestion(self.questions_storage)

    def add_checkbutton_question_btn_click(self):
        AddCheckButtonQuestion(self.questions_storage)

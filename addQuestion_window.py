from tkinter import *
from typing import List
from questionsStrorage import QuestionsStorage
from answer import Answer
from add_baseQuestion_window import AddBaseQuestionWindow
from add_radioButtonQuestion_window import AddRadioButtonQuestion
from add_checkButtonQuestion_window import AddCheckButtonQuestion
import customtkinter


# Настройка внешнего вида и темы GUI-окна
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")


class AddQuestionWindow(customtkinter.CTk):
    """Класс AddQuestionWindow - инициализирует окно с выбором типа вопроса, который нужно добавить."""
    def __init__(self, questions_storage: QuestionsStorage):
        """Устанавливает все необходимые атрибуты для объекта AddQuestionWindow."""
        super().__init__()
        self.answers: List[Answer] = []
        self.questions_storage = questions_storage
        self.title('Добавление вопроса')
        self.geometry('250x250')
        self.resizable(False, True)

        # Создание рамки для кнопок
        self.buttons_frame = customtkinter.CTkFrame(self)
        self.buttons_frame.pack(padx=10, pady=(10, 10))

        self.add_baseQuestion_btn = customtkinter.CTkButton(self.buttons_frame, text="Добавить базовый вопрос",
                                           command=self._add_base_question_btn_click, height=60, width=190)
        self.add_baseQuestion_btn.pack(padx=10, pady=(10, 0))

        self.add_radioButtonQuestion_btn = customtkinter.CTkButton(self.buttons_frame, text="Добавить вопрос с выбором",
                                                  command=self._add_radiobutton_question_btn_click, height=60, width=190)
        self.add_radioButtonQuestion_btn.pack(padx=10, pady=(10, 0))

        self.add_checkButtonQuestion_btn = customtkinter.CTkButton(self.buttons_frame,
                                                  text="Добавить вопрос \n с множественным выбором",
                                                  command=self._add_checkbutton_question_btn_click, height=60, width=190)
        self.add_checkButtonQuestion_btn.pack(padx=10, pady=(10, 10))

        self.mainloop()

    def _add_base_question_btn_click(self):
        """Обработчик нажатия кнопки add_base_question_btn - создаёт объект класса AddBaseQuestionWindow."""
        AddBaseQuestionWindow(self.questions_storage)

    def _add_radiobutton_question_btn_click(self):
        """Обработчик нажатия кнопки add_radiobutton_question_btn - создаёт объект класса AddRadioButtonQuestion."""
        AddRadioButtonQuestion(self.questions_storage)

    def _add_checkbutton_question_btn_click(self):
        """Обработчик нажатия кнопки add_checkbutton_question_btn - создаёт объект класса AddCheckButtonQuestion."""
        AddCheckButtonQuestion(self.questions_storage)

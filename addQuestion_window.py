from tkinter import *
from typing import List
from questionsStrorage import QuestionsStorage
from answer import Answer
from add_baseQuestion_window import AddBaseQuestionWindow
from add_radioButtonQuestion_window import AddRadioButtonQuestion
from add_checkButtonQuestion_window import AddCheckButtonQuestion
from user import User
from window import Window
import admin_menu_window
import customtkinter


class AddQuestionWindow(Window):
    """Класс AddQuestionWindow - инициализирует окно с выбором типа вопроса, который нужно добавить."""
    def __init__(self, questions_storage: QuestionsStorage, user: User):
        """Устанавливает все необходимые атрибуты для объекта AddQuestionWindow."""
        super().__init__()

        self.answers: List[Answer] = []
        self.questions_storage = questions_storage
        self.user = user

        self.title('Добавление вопроса')
        self.width = 240
        self.height = 290
        self.resizable(False, True)

        self._place()

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

        self.back_to_menu_btn = customtkinter.CTkButton(self, text='Вернуться в меню',
                                                        command=self.back_to_menu_btn_click, width=70)
        self.back_to_menu_btn.pack(padx=20, pady=(10, 10), anchor="se")


        self.mainloop()

    def _add_base_question_btn_click(self):
        """Обработчик нажатия кнопки add_base_question_btn - создаёт объект класса AddBaseQuestionWindow."""
        self.withdraw()
        AddBaseQuestionWindow(self.questions_storage, self.user)
        self.destroy()

    def _add_radiobutton_question_btn_click(self):
        """Обработчик нажатия кнопки add_radiobutton_question_btn - создаёт объект класса AddRadioButtonQuestion."""
        self.withdraw()
        AddRadioButtonQuestion(self.questions_storage, self.user)
        self.destroy()

    def _add_checkbutton_question_btn_click(self):
        """Обработчик нажатия кнопки add_checkbutton_question_btn - создаёт объект класса AddCheckButtonQuestion."""
        self.withdraw()
        AddCheckButtonQuestion(self.questions_storage, self.user)
        self.destroy()

    def back_to_menu_btn_click(self):
        """Обработчик нажатия кнопки back_to_menu_btn - удаляет данное окно и создаёт объект MenuWindow."""
        self.withdraw()
        menu_window.AdminMenuWindow(self.user)
        self.destroy()

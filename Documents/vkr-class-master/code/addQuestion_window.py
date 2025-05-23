from tkinter import *
from typing import List
from questionsStrorage import QuestionsStorage
from answer import Answer
from add_baseQuestion_window import AddBaseQuestionWindow
from add_radioButtonQuestion_window import AddRadioButtonQuestion
from add_checkButtonQuestion_window import AddCheckButtonQuestion


base_padding = {'padx': 10, 'pady': 8}


class AddQuestionWindow:
    """Класс AddQuestionWindow - инициализирует окно с выбором типа вопроса, который нужно добавить."""
    def __init__(self, questions_storage: QuestionsStorage):
        """Устанавливает все необходимые атрибуты для объекта AddQuestionWindow."""
        self.answers: List[Answer] = []
        self.questions_storage = questions_storage
        self.addQuestion_window = Tk()
        self.addQuestion_window.title('Добавление вопроса')
        self.addQuestion_window.geometry('300x150')
        self.addQuestion_window.resizable(False, True)
        self.selected_id = IntVar(self.addQuestion_window)

        self.add_baseQuestion_btn = Button(self.addQuestion_window, text="Добавить базовый вопрос",
                                           command=self._add_base_question_btn_click, width=50)
        self.add_baseQuestion_btn.pack(**base_padding)

        self.add_radioButtonQuestion_btn = Button(self.addQuestion_window, text="Добавить вопрос с выбором",
                                                  command=self._add_radiobutton_question_btn_click, width=50)
        self.add_radioButtonQuestion_btn.pack(**base_padding)

        self.add_checkButtonQuestion_btn = Button(self.addQuestion_window,
                                                  text="Добавить вопрос с множественным выбором",
                                                  command=self._add_checkbutton_question_btn_click, width=50)
        self.add_checkButtonQuestion_btn.pack(**base_padding)

    def _add_base_question_btn_click(self):
        """Обработчик нажатия кнопки add_base_question_btn - создаёт объект класса AddBaseQuestionWindow."""
        AddBaseQuestionWindow(self.questions_storage)

    def _add_radiobutton_question_btn_click(self):
        """Обработчик нажатия кнопки add_radiobutton_question_btn - создаёт объект класса AddRadioButtonQuestion."""
        AddRadioButtonQuestion(self.questions_storage)

    def _add_checkbutton_question_btn_click(self):
        """Обработчик нажатия кнопки add_checkbutton_question_btn - создаёт объект класса AddCheckButtonQuestion."""
        AddCheckButtonQuestion(self.questions_storage)

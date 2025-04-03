from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from user import User
from questionsStrorage import QuestionsStorage
from addQuestion_window import AddQuestionWindow
from deleteQuestion_window import DeleteQuestionWindow
from test_window import TestWindow
from results_window import ResultsWindow
from fileProvider import FileProvider
from create_newtest_window import CreateNewTestWindow
import os
import customtkinter


# Настройка внешнего вида и темы GUI-окна
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")


class MenuWindow(customtkinter.CTk):
    """Класс MenuWindow - инициализирует окно меню."""
    def __init__(self, user: User):
        """Устанавливает все необходимые атрибуты для объекта MenuWindow."""
        super().__init__()
        self.user = user

        self.questions_storage = QuestionsStorage("Tests/base_test.json")
        self.title("Меню")
        self.geometry('800x400')
        self.resizable(False, False)

        self.tests = FileProvider.get_test_names()

        self.test_var = StringVar(self, value="base_test")

        self.tests_combobox = customtkinter.CTkComboBox(self, variable=self.test_var, values=self.tests,
                                           state="readonly")
        self.tests_combobox.pack(anchor=NW, padx=6, pady=6)
        self.tests_combobox.bind("<<ComboboxSelected>>", self._selected_test)

        # Создание рамки для кнопок
        self.buttons_frame = customtkinter.CTkFrame(self)
        self.buttons_frame.pack(padx=10, pady=(10, 0))

        self.create_newtest_btn = customtkinter.CTkButton(self.buttons_frame, text='Создать новый тест',
                                                          command=self._create_newtest_btn_click, height=40, width=150)
        self.create_newtest_btn.pack(padx=10, pady=(10, 0))

        self.addQuestion_btn = customtkinter.CTkButton(self.buttons_frame, text='Добавить вопрос',
                                                       command=self._add_question_btn_clicked, height=40, width=150)
        self.addQuestion_btn.pack(padx=10, pady=(10, 0))

        self.deleteQuestion_btn = customtkinter.CTkButton(self.buttons_frame, text='Удалить вопрос',
                                                          command=self._delete_question_btn_clicked, height=40, width=150)
        self.deleteQuestion_btn.pack(padx=10, pady=(10, 0))

        self.test_btn = customtkinter.CTkButton(self.buttons_frame, text='Начать тест',
                                                command=self._test_menu_btn_clicked, height=40, width=150)
        self.test_btn.pack(padx=10, pady=(10, 0))

        self.show_results_btn = customtkinter.CTkButton(self.buttons_frame, text="Результаты",
                                                        command=self._show_results_btn_click, height=40, width=150)
        self.show_results_btn.pack(padx=10, pady=(10, 10))

        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.mainloop()

    def _create_newtest_btn_click(self):
        """Обработчик нажатия кнопки create_newtest_btn - создаёт объект класса CreateNewTestWindow."""
        self.withdraw()
        CreateNewTestWindow(self.user, self.questions_storage)
        self.destroy()

    def _selected_test(self, event):
        """Обработчик выбранного теста, запускает выбранный тест."""
        test_name = self.test_var.get()
        test_path = FileProvider.find_test_path(test_name)

        self.questions_storage.update_test(test_path)


    @staticmethod
    def _show_results_btn_click():
        """Обработчик нажатия кнопки show_results_btn - создаёт объект класса ResultsWindow."""
        ResultsWindow()

    def _add_question_btn_clicked(self):
        """Обработчик нажатия кнопки add_question_btn - создаёт объект класса AddQuestionWindow."""
        self.withdraw()
        AddQuestionWindow(self.questions_storage, self.user)
        self.destroy()

    def _delete_question_btn_clicked(self):
        """Обработчик нажатия кнопки delete_question_btn - создаёт объект класса DeleteQuestionWindow."""
        self.withdraw()
        DeleteQuestionWindow(self.questions_storage, self.user)
        self.destroy()

    def _test_menu_btn_clicked(self):
        """Обработчик нажатия кнопки test_menu_btn - при наличии вопросов в тесте создаёт объект класса TestWindow."""
        if len(self.questions_storage.test.questions) == 0:
            messagebox.showwarning(title="Предупреждение", message="В тесте нет вопросов. Сначала добавьте их.")
            return

        selected_name = f'{self.test_var.get()}.json'
        TestWindow(self.user, self.questions_storage, selected_name)

    @staticmethod
    def on_closing():
        """Используется в протоколе окна, закрывает приложение при закрытии окна."""
        exit()

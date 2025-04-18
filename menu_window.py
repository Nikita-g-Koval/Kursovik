from tkinter import *
from tkinter import messagebox
from user import User
from questionsStrorage import QuestionsStorage
from addQuestion_window import AddQuestionWindow
from deleteQuestion_window import DeleteQuestionWindow
from test_window import TestWindow
from results_window import ResultsWindow
from fileProvider import FileProvider
from create_newtest_window import CreateNewTestWindow
from window import Window
import customtkinter


class MenuWindow(Window):
    """Класс MenuWindow - инициализирует окно меню."""
    def __init__(self, user: User, question_storage: QuestionsStorage = QuestionsStorage("base_test")):
        """Устанавливает все необходимые атрибуты для объекта MenuWindow."""
        super().__init__()

        self.user = user
        self.questions_storage = question_storage

        self.title("Меню")
        self.width = 800
        self.height = 400
        self.resizable(False, False)

        self._place()

        self.tests = FileProvider.get_test_names()

        self.test_var = StringVar(self, value=self.questions_storage.test.name)

        self.tests_combobox = customtkinter.CTkComboBox(self, variable=self.test_var, values=self.tests,
                                           state="readonly", command=self._selected_test)
        self.tests_combobox.pack(anchor=NW, padx=6, pady=6)


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


        self.mainloop()

    def _create_newtest_btn_click(self):
        """Обработчик нажатия кнопки create_newtest_btn - создаёт объект класса CreateNewTestWindow."""
        self.withdraw()
        CreateNewTestWindow(self.user, self.questions_storage)

    def _selected_test(self, event):
        """Обработчик выбранного теста, запускает выбранный тест."""
        selected_test_name = self.test_var.get()
        self._select_test(selected_test_name)

    def _select_test(self, test_name):
        """Обновляет список вопросов по переданному имени теста."""
        test_path = FileProvider.find_test_path(test_name)

        self.questions_storage.update_test(test_path)


    def _show_results_btn_click(self):
        """Обработчик нажатия кнопки show_results_btn - создаёт объект класса ResultsWindow."""
        ResultsWindow(self.user)

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

        self.withdraw()
        TestWindow(self.user, self.questions_storage)
        self.destroy()

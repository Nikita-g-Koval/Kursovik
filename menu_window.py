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


font_header = ('Arial', 15)
font_entry = ('Arial', 12)
lable_font = ('Arial', 11)
base_padding = {'padx': 10, 'pady': 8}
header_padding = {'padx': 10, 'pady': 12}


class MenuWindow:
    """Класс MenuWindow - инициализирует окно меню."""
    def __init__(self, user: User):
        """Устанавливает все необходимые атрибуты для объекта MenuWindow."""
        self.user = user

        self.questions_storage = QuestionsStorage("Tests/base_test.json")
        self.menu_window = Tk()
        self.menu_window.title("Меню")
        self.menu_window.geometry('400x300')
        self.menu_window.resizable(False, False)

        self.tests = FileProvider.get_test_names()

        self.test_var = StringVar(self.menu_window, value="base_test")

        self.tests_combobox = ttk.Combobox(self.menu_window, textvariable=self.test_var, values=self.tests,
                                           state="readonly")
        self.tests_combobox.pack(anchor=NW, padx=6, pady=6)
        self.tests_combobox.bind("<<ComboboxSelected>>", self._selected_test)

        self.create_newtest_btn = Button(self.menu_window, text='Создать новый тест',
                                         command=self._create_newtest_btn_click, width=15)
        self.create_newtest_btn.pack(**base_padding)

        self.addQuestion_btn = Button(self.menu_window, text='Добавить вопрос', command=self._add_question_btn_clicked,
                                      width=15)
        self.addQuestion_btn.pack(**base_padding)

        self.deleteQuestion_btn = Button(self.menu_window, text='Удалить вопрос',
                                         command=self._delete_question_btn_clicked, width=15)
        self.deleteQuestion_btn.pack(**base_padding)

        self.test_btn = Button(self.menu_window, text='Начать тест',
                               command=self._test_menu_btn_clicked, width=15)
        self.test_btn.pack(**base_padding)

        self.show_results_btn = Button(self.menu_window, text="Результаты", command=self._show_results_btn_click,
                                       width=15)
        self.show_results_btn.pack(**base_padding)

        self.menu_window.protocol("WM_DELETE_WINDOW", self.on_closing)

    def _create_newtest_btn_click(self):
        """Обработчик нажатия кнопки create_newtest_btn - создаёт объект класса CreateNewTestWindow."""
        self.menu_window.withdraw()
        CreateNewTestWindow(self.user, self.questions_storage)
        self.menu_window.destroy()

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
        AddQuestionWindow(self.questions_storage)

    def _delete_question_btn_clicked(self):
        """Обработчик нажатия кнопки delete_question_btn - создаёт объект класса DeleteQuestionWindow."""
        DeleteQuestionWindow(self.questions_storage)

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

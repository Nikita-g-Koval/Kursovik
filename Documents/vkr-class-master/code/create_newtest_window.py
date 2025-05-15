from tkinter import *
from tkinter import messagebox
from typing import List
from question import Question
from user import User
from test import Test
from questionsStrorage import QuestionsStorage
from fileProvider import FileProvider
import menu_window


base_padding = {'padx': 10, 'pady': 8}


class CreateNewTestWindow:
    """Класс CreateNewTestWindow - инициализирует окно для создания нового теста."""
    path = None

    def __init__(self, user: User, question_storage: QuestionsStorage):
        """Устанавливает все необходимые атрибуты для объекта CreateNewTestWindow."""
        self.user = user
        self.qs = question_storage

        self.create_newtest_window = Tk()
        self.create_newtest_window.title("Меню")
        self.create_newtest_window.geometry('200x250')
        self.create_newtest_window.resizable(False, False)

        self.testname_label = Label(self.create_newtest_window, text='Название теста')
        self.testname_label.pack(**base_padding)

        self.testname_entry = Entry(self.create_newtest_window, width=30)
        self.testname_entry.pack(**base_padding)

        self.create_newtest_btn = Button(self.create_newtest_window, text='Создать тест',
                                         command=self.create_newtest_btn_click, width=20)
        self.create_newtest_btn.pack(**base_padding)

        self.create_base_test_btn = Button(self.create_newtest_window, text='Создать базовый тест',
                                           command=self.create_base_test_btn_click, width=20)
        self.create_base_test_btn.pack(**base_padding)

        self.back_to_menu_btn = Button(self.create_newtest_window, text='Вернуться в меню',
                                       command=self.back_to_menu_btn_click, width=20)
        self.back_to_menu_btn.pack(**base_padding)

        self.create_newtest_window.protocol("WM_DELETE_WINDOW", self.on_closing)

    def create_base_test_btn_click(self):
        """Обработчик нажатия кнопки create_base_test_btn - создаёт тест с базовым набором вопросов."""
        testname = self.testname_entry.get()

        if len(testname) == 0:
            messagebox.showwarning(message='Введите название теста!', title='Предупреждение')
            return

        self._create_test(self.qs.test.questions, testname)
        messagebox.showinfo(title="Уведомление", message="Тест успешно создан")

    def create_newtest_btn_click(self):
        """Обработчик нажатия кнопки create_newtest_btn - создаёт пустой тест."""
        testname = self.testname_entry.get()

        if len(testname) == 0:
            messagebox.showwarning(message='Введите название теста!', title='Предупреждение')
            return

        self._create_test([], testname)
        messagebox.showinfo(title="Уведомление", message="Тест успешно создан")

    @staticmethod
    def _create_test(questions: List[Question], test_name: str):
        """Создаёт тест с указанными вопросами и именем."""
        test = Test(test_name, questions)
        FileProvider.save_test(test)

    def back_to_menu_btn_click(self):
        """Обработчик нажатия кнопки back_to_menu_btn - удаляет данное окно и создаёт объект MenuWindow."""
        self.create_newtest_window.withdraw()
        menu_window.MenuWindow(self.user)
        self.create_newtest_window.destroy()

    @staticmethod
    def on_closing():
        """Используется в протоколе окна, закрывает приложение при закрытии окна."""
        exit()

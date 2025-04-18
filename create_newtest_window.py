from tkinter import messagebox
from typing import List
from question import Question
from user import User
from test import Test
from questionsStrorage import QuestionsStorage
from fileProvider import FileProvider
from window import Window
import menu_window
import customtkinter


class CreateNewTestWindow(Window):
    """Класс CreateNewTestWindow - инициализирует окно для создания нового теста."""
    path = None

    def __init__(self, user: User, question_storage: QuestionsStorage):
        """Устанавливает все необходимые атрибуты для объекта CreateNewTestWindow."""
        super().__init__()
        self.user = user
        self.qs = question_storage

        self.title("Меню")
        self.width = 420
        self.height = 230
        self.resizable(False, False)

        self._place()

        # Создание рамки для строк ввода
        self.inputs_frame = customtkinter.CTkFrame(self)
        self.inputs_frame.pack(padx=10, pady=(10, 0))

        # Создание рамки для кнопок
        self.buttons_frame = customtkinter.CTkFrame(self)
        self.buttons_frame.pack(padx=10, pady=(10, 10))

        self.testname_label = customtkinter.CTkLabel(self.inputs_frame, text='Название теста')
        self.testname_label.pack(padx=10, pady=(10, 0))

        self.testname_entry = customtkinter.CTkEntry(self.inputs_frame, width=390, height=30)
        self.testname_entry.pack(padx=10, pady=(10, 10))

        self.create_newtest_btn = customtkinter.CTkButton(self.buttons_frame, text='Создать тест',
                                         command=self.create_newtest_btn_click, height=40, width=150)
        self.create_newtest_btn.grid(row=0, column=0, padx=(10,0), pady=(10, 10), sticky="nsw")

        self.create_base_test_btn = customtkinter.CTkButton(self.buttons_frame, text='Создать тест на основе текущего',
                                           command=self.create_base_test_btn_click, height=40, width=150)
        self.create_base_test_btn.grid(row=0, column=1, padx=(10,10), pady=(10, 10), sticky="nsw")

        self.back_to_menu_btn = customtkinter.CTkButton(self, text='Вернуться в меню',
                                       command=self.back_to_menu_btn_click, width=70)
        self.back_to_menu_btn.pack(padx=10, pady=(10, 10), anchor="se")


        self.mainloop()

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
        self.withdraw()
        menu_window.MenuWindow(self.user)
        self.destroy()

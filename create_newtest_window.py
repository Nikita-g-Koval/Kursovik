from tkinter import *
from tkinter import messagebox
from typing import List
from question import Question
from user import User
from questionsStrorage import QuestionsStorage
from fileProvider import FileProvider
import menu_window


class CreateNewTestWindow:
    path = None
    def __init__(self, user: User, question_storage: QuestionsStorage):
        self.user = user
        self.qs = question_storage

        self.create_newtest_window = Tk()
        self.create_newtest_window.title("Меню")
        self.create_newtest_window.geometry('200x150')
        self.create_newtest_window.resizable(False, False)

        self.testname_label = Label(self.create_newtest_window, text='Название теста')
        self.testname_label.pack()

        self.testname_entry = Entry(self.create_newtest_window, width=30)
        self.testname_entry.pack()

        self.create_newtest_btn = Button(self.create_newtest_window, text='Создать тест',
                                         command=self.create_newtest_btn_click)
        self.create_newtest_btn.pack()

        self.create_base_test_btn = Button(self.create_newtest_window, text='Создать базовый тест',
                                           command=self.create_base_test_btn_click)
        self.create_base_test_btn.pack()

        self.back_to_menu_btn = Button(self.create_newtest_window, text='Вернуться в меню',
                                       command=self.back_to_menu_btn_click)
        self.back_to_menu_btn.pack()

        self.create_newtest_window.protocol("WM_DELETE_WINDOW", self.on_closing)

    def create_base_test_btn_click(self):
        testname = self.testname_entry.get()

        if len(testname) == 0:
            messagebox.showwarning(message='Введите название теста!', title='Предупреждение')
            return

        self._create_test(self.qs.base_questions, testname)
        messagebox.showinfo(title="Уведомление", message="Тест успешно создан")

    def create_newtest_btn_click(self):
        testname = self.testname_entry.get()

        if len(testname) == 0:
            messagebox.showwarning(message='Введите название теста!', title='Предупреждение')
            return

        self._create_test([], testname)
        messagebox.showinfo(title="Уведомление", message="Тест успешно создан")

    @staticmethod
    def _create_test(questions: List[Question], test_name: str):
        FileProvider.save_test(questions, test_name)

    def back_to_menu_btn_click(self):
        self.create_newtest_window.withdraw()
        menu_window.MenuWindow(self.user)
        self.create_newtest_window.destroy()

    @staticmethod
    def on_closing():
        exit()

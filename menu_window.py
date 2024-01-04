from tkinter import *
from tkinter import ttk
from user import User
from questionsStrorage import QuestionsStorage
from addQuestion_window import AddQuestionWindow
from deleteQuestion_window import DeleteQuestionWindow
from test_window import TestWindow
from results_window import ResultsWindow
from fileProvider import FileProvider
import os


font_header = ('Arial', 15)
font_entry = ('Arial', 12)
lable_font = ('Arial', 11)
base_padding = {'padx': 10, 'pady': 8}
header_padding = {'padx': 10, 'pady': 12}


class MenuWindow:
    def __init__(self, user: User):
        self.user = user
        self.questions_storage = QuestionsStorage()
        self.menu_window = Tk()
        self.menu_window.title("Меню")
        self.menu_window.geometry('600x600')
        self.menu_window.resizable(False, False)

        self.addQuestion_btn = Button(self.menu_window, text='Добавить вопрос', command=self.add_question_btn_clicked)
        self.addQuestion_btn.pack(**base_padding)

        self.deleteQuestion_btn = Button(self.menu_window, text='Удалить вопрос',
                                         command=self.delete_question_btn_clicked)
        self.deleteQuestion_btn.pack(**base_padding)

        self.test_btn = Button(self.menu_window, text='Начать тест',
                               command=self.test_menu_btn_clicked)
        self.test_btn.pack(**base_padding)

        self.show_results_btn = Button(self.menu_window, text="Результаты", command=self.show_results_btn_click)
        self.show_results_btn.pack(**base_padding)

        self.tests = FileProvider.get_tests()
        for i in range(0, len(self.tests)):
            self.tests[i] = self.tests[i].replace('.json', '')

        self.test_var = StringVar(self.menu_window)

        self.tests_combobox = ttk.Combobox(self.menu_window, textvariable=self.test_var, values=self.tests,
                                           state="readonly")
        self.tests_combobox.pack(anchor=NW, padx=6, pady=6)
        self.tests_combobox.bind("<<ComboboxSelected>>", self._selected_test)

        self.menu_window.protocol("WM_DELETE_WINDOW", self.on_closing)

    def _selected_test(self, event):
        test_name = f'{self.test_var.get()}.json'
        tests_folder_path = os.path.abspath('Tests')
        test_path = f'{tests_folder_path}\\{test_name}'

        self.questions_storage.update_questions(test_path)

    @staticmethod
    def show_results_btn_click():
        ResultsWindow()

    def add_question_btn_clicked(self):
        AddQuestionWindow(self.questions_storage)

    def delete_question_btn_clicked(self):
        DeleteQuestionWindow(self.questions_storage)

    def test_menu_btn_clicked(self):
        selected_name = f'{self.test_var.get()}.json'
        TestWindow(self.user, self.questions_storage, selected_name)

    @staticmethod
    def on_closing():
        exit()

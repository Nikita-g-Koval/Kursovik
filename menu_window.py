from tkinter import *
from user import User
from questionsStorage import QuestionsStorage
from addQuestion_window import AddQuestionWindow
from deleteQuestion_window import DeleteQuestionWindow
from test_window import TestWindow


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
        self.menu_window.geometry('400x300')
        self.menu_window.resizable(False, False)

        self.addQuestion_btn = Button(self.menu_window, text='Добавить вопрос', command=self.add_question_btn_clicked)
        self.addQuestion_btn.pack(**base_padding)

        self.deleteQuestion_btn = Button(self.menu_window, text='Удалить вопрос',
                                         command=self.delete_question_btn_clicked)
        self.deleteQuestion_btn.pack(**base_padding)

        self.test_btn = Button(self.menu_window, text='Начать тест',
                                         command=self.test_menu_btn_clicked)
        self.test_btn.pack(**base_padding)

        self.menu_window.protocol("WM_DELETE_WINDOW", self.on_closing)

    def add_question_btn_clicked(self):
        AddQuestionWindow(self.questions_storage)

    def delete_question_btn_clicked(self):
        DeleteQuestionWindow(self.questions_storage)

    def test_menu_btn_clicked(self):
        TestWindow(self.user, self.questions_storage)

    @staticmethod
    def on_closing():
        exit()
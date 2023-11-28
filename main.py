import os
import json
from random import random
from tkinter import *
from tkinter import messagebox
from validation import Validation
from user import User
from questionsStrorage import QuestionsStorage
from diagnosesStorage import DiagnosesStorage
from fileProvider import FileProvider
from question import Question
from tkinter.scrolledtext import ScrolledText


main_window = Tk()
main_window.title("Авторизация")
main_window.geometry('450x230')
main_window.resizable(False, False)

font_header = ('Arial', 15)
font_entry = ('Arial', 12)
lable_font = ('Arial',  11)
base_padding = {'padx': 10, 'pady': 8}
header_padding = {'padx': 10, 'pady': 12}


class menuWindow:
    def __init__(self, user: User):
        self.user = user
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

        self.menu_window.protocol("WM_DELETE_WINDOW", on_closing)

    def add_question_btn_clicked(self):
        self.menu_window.withdraw()
        addQuestionWindow()

    def delete_question_btn_clicked(self):
        self.menu_window.withdraw()
        DeleteQuestionWindow()

    def test_menu_btn_clicked(self):
        self.menu_window.withdraw()
        testWindow(self.user)


def on_closing():
    exit()


class addQuestionWindow:
    def __init__(self):
        self.new_question = None
        self.questions_storage = QuestionsStorage()
        self.addQuestion_window = Tk()
        self.addQuestion_window.title('Добавление вопроса')
        self.addQuestion_window.geometry('400x100')
        self.addQuestion_window.resizable(False, False)

        Label(self.addQuestion_window, text="Текст вопроса:", justify=LEFT).grid(row=0, column=0, sticky=W)
        self.questionText_entry = Entry(self.addQuestion_window, width=30)
        self.questionText_entry.grid(row=0, column=1, sticky=EW)

        Label(self.addQuestion_window, text="Ответ на вопрос:", justify=LEFT).grid(row=1, column=0, sticky=W)
        self.answer_entry = Entry(self.addQuestion_window, width=30)
        self.answer_entry.grid(row=1, column=1, sticky=EW)

        self.add_question_btn = Button(self.addQuestion_window, text='Добавить вопрос',
                                       command=self.add_question_btn_click)
        self.add_question_btn.grid(row=2, sticky=W+E)

        self.save_changes_btn = Button(self.addQuestion_window, text='Сохранить изменения',
                                       command=self.save_changes_btn_click)
        self.save_changes_btn.grid(row=3, sticky=W+E)

        self.addQuestion_window.protocol("WM_DELETE_WINDOW", on_closing)

    def add_question_btn_click(self):
        question_text = self.questionText_entry.get()
        answer = self.answer_entry.get()

        if not Validation.ValidateQuestion(question_text):
            messagebox.showwarning(title="Предупреждение",
                                   message="Введены некорректные данные! Введите текст вопроса.")
            return

        if not Validation.ValidateAnswer(answer):
            messagebox.showwarning(title="Предупреждение",
                                   message="Введены некорректные данные! Введите целочисленный ответ на вопрос." )
            return

        self.new_question = Question(question_text, answer)
        self.questions_storage.add_question(self.new_question)
        messagebox.showinfo(title="Успешно", message="Вопрос добавлен.")

    def save_changes_btn_click(self):
        FileProvider.save_questions(self.questions_storage.questions)
        messagebox.showinfo(title="Успешно", message="Изменения сохранены.")


# доделать
class DeleteQuestionWindow:
    def __init__(self):
        self.questions_storage = QuestionsStorage()
        self.deleteQuestion_window = Tk()
        self.deleteQuestion_window.title('Удаление вопроса')
        self.deleteQuestion_window.geometry('600x700')
        self.deleteQuestion_window.resizable(True, True)

        self.questions_editor = ScrolledText(self.deleteQuestion_window, wrap="word")
        self.questions_editor.pack(fill=BOTH, expand=1)

        self.print_questions()

        self.questionNumber_entry = Entry(self.deleteQuestion_window, bg='#fff', fg='#444', font=font_entry)
        self.questionNumber_entry.pack()

        self.delete_question_btn = Button(self.deleteQuestion_window,
                                          text='Удалить вопрос', command=self.delete_question_btn_click)
        self.delete_question_btn.pack()

        self.save_changes_btn = Button(self.deleteQuestion_window,
                                       text='Сохранить изменения', command=self.save_changes_btn_click)
        self.save_changes_btn.pack()

        self.deleteQuestion_window.protocol("WM_DELETE_WINDOW", on_closing)

    def delete_question_btn_click(self):
        question_number = self.questionNumber_entry.get()
        if not question_number.isdigit():
            messagebox.showwarning(title="Предупреждение", message="Введите номер вопроса, целое число.")
            return
        number = int(question_number)

        if number < 1 or number >= self.count:
            messagebox.showwarning(title="Предупреждение",
                                   message="Номер вопроса выходит за границу количества вопросов.")
            return

        self.questions_storage.remove_question(number)
        self.print_questions()
        messagebox.showinfo(title="Уведомление", message="Вопрос успешно удалён. Сохраните изменения.")


    def save_changes_btn_click(self):
        FileProvider.save_questions(self.questions)
        messagebox.showinfo(title="Уведомление", message="Изменения сохранены.")

    def print_questions(self):
        self.questions_editor.delete('1.0', END)
        self.questions = self.questions_storage.questions
        self.count = 1
        for q in self.questions:
            self.questions_editor.insert(END, "№{i} {question}\n".format(i=self.count, question=q.text))
            self.count += 1

class testWindow:
    def __init__(self, user: User):
        self.user = user
        self.test_window = Tk()
        self.test_window.title("Тест")
        self.test_window.geometry('800x300')
        self.test_window.resizable(False, False)

        self.diagnoses = DiagnosesStorage()
        self.qs = QuestionsStorage()
        self.questions = self.qs.shuffle()
        self.questionId = 0

        self.test_label = Label(self.test_window, text="Вопрос №{0}:".format(self.questionId + 1)
                                                       + self.questions[self.questionId].text, font=font_entry,
                                justify=CENTER, **header_padding)
        self.test_label.pack()

        self.userAnswer_entry = Entry(self.test_window, bg='#fff', fg='#444', font=font_entry)
        self.userAnswer_entry.pack()

        self.acceptAnswer_btn = Button(self.test_window, text='Ответить', command=self.accept_answer_btn_clicked)
        self.acceptAnswer_btn.pack(**base_padding)

        self.test_window.protocol("WM_DELETE_WINDOW", on_closing)

    def accept_answer_btn_clicked(self):
        input_answer = self.userAnswer_entry.get()
        if not Validation.ValidateAnswer(input_answer):
            messagebox.showwarning(
                title="Предупреждение",
                message="Введены некорректные данные! Введите целочисленное число в разумных пределах.")
            return
        if int(input_answer) == self.questions[self.questionId].answer:
            self.user.rightAnswersCount += 1
        if self.questionId >= len(self.questions)-1:
            diagnosis = self.diagnoses.calculate_diagnose(len(self.questions), self.user.rightAnswersCount)
            messagebox.showinfo(title="Тест завершён", message="{0}, ваш диагноз: {1}".format(self.user.name,
                                                                                              diagnosis.grade))
            return
        self.userAnswer_entry.delete(0, END)
        self.questionId += 1
        self.show_next_question()

    def show_next_question(self):
        self.test_label.config(text="Вопрос №{0}:".format(self.questionId+1) + self.questions[self.questionId].text)


def clicked():
    inputname = username_entry.get()
    if not Validation.ValidateUserName(username=inputname):
        messagebox.showwarning(
            title="Предупреждение",
            message="Введённое имя некорректно! Длина имени не меньше 2 символов. Разрешены только буквы.")
        return
    user = User(inputname)
    main_window.withdraw()
    menuWindow(user)


main_label = Label(main_window, text='Авторизация', font=font_header, justify=CENTER, **header_padding)
main_label.pack()

username_entry = Entry(main_window, bg='#fff', fg='#444', font=font_entry)
username_entry.pack()

send_btn = Button(main_window, text='Перейти в меню', command=clicked)
send_btn.pack(**base_padding)

main_window.mainloop()












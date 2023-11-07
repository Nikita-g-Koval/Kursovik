import os
import json
from random import random
from tkinter import *
from tkinter import messagebox
from validation import Validation
from user import User
from questionsStrorage import QuestionStorage
from diagnosesStorage import DiagnosesStorage


main_window = Tk()
main_window.title("Авторизация")
main_window.geometry('450x230')
main_window.resizable(False, False)

font_header = ('Arial', 15)
font_entry = ('Arial', 12)
lable_font = ('Arial',  11)
base_padding = {'padx': 10, 'pady': 8}
header_padding = {'padx': 10, 'pady': 12}

user: User



class testWindow:
    def __init__(self, user: User):
        self.user = user
        self.testWindow = Tk()
        self.testWindow.title("Тест")
        self.testWindow.geometry('800x300')
        self.testWindow.resizable(False, False)

        self.diagnoses = DiagnosesStorage()
        self.qs = QuestionStorage()
        self.questions = self.qs.Shuffle()
        self.questionId = 0

        self.test_label = Label(self.testWindow, text="Вопрос №{0}:".format(self.questionId+1) + self.questions[self.questionId].text, font=font_entry, justify=CENTER, **header_padding)
        self.test_label.pack()

        self.userAnswer_entry = Entry(self.testWindow, bg='#fff', fg='#444', font=font_entry)
        self.userAnswer_entry.pack()

        self.acceptAnswer_btn = Button(self.testWindow, text='Ответить', command=self.acceptAnswer_btn_clicked)
        self.acceptAnswer_btn.pack(**base_padding)

        self.testWindow.protocol("WM_DELETE_WINDOW", self.on_closing)

    def acceptAnswer_btn_clicked(self):
        inputAnswer = self.userAnswer_entry.get()
        if not Validation.ValidateAnswer(inputAnswer):
            messagebox.showwarning(title="Предупреждение", message="Введены некорректные данные! Введите целочисленное число в разумных пределах.")
            return
        if int(inputAnswer) == self.questions[self.questionId].answer:
            self.user.rightAnswersCount += 1
        if self.questionId >= len(self.questions)-1:
            diagnosis = self.diagnoses.CalculateDiagnose(len(self.questions), self.user.rightAnswersCount)
            messagebox.showinfo(title="Тест завершён", message="{0}, ваш диагноз: {1}".format(self.user.name, diagnosis.grade))
            return
        self.questionId += 1
        self.showNextQuestion()

    def showNextQuestion(self):
        self.test_label.config(text="Вопрос №{0}:".format(self.questionId+1) + self.questions[self.questionId].text)




    def on_closing(self):
        exit()


def clicked():
    inputname = username_entry.get()
    if not Validation.ValidateUserName(username=inputname):
        messagebox.showwarning(title="Предупреждение", message="Введённое имя некорректно! Длина имени не меньше 2 символов. Разрешены только буквы.")
        return
    user = User(inputname)
    main_window.withdraw()
    testWindow(user)


main_label = Label(main_window, text='Авторизация', font=font_header, justify=CENTER, **header_padding)
main_label.pack()

username_entry = Entry(main_window, bg='#fff', fg='#444', font=font_entry)
username_entry.pack()

send_btn = Button(main_window, text='Перейти к тесту', command=clicked)
send_btn.pack(**base_padding)

main_window.mainloop()












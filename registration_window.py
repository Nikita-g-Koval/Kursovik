from tkinter import *
from tkinter import messagebox
from validation import Validation
from user import User
from menu_window import MenuWindow
from fileProvider import FileProvider
import os

font_header = ('Arial', 15)
font_entry = ('Arial', 12)
lable_font = ('Arial', 11)
base_padding = {'padx': 10, 'pady': 8}
header_padding = {'padx': 10, 'pady': 12}


class RegistrationWindow:
    """Класс RegistrationWindow - инициализирует окно регистрации пользователя."""
    def __init__(self):
        """Устанавливает все необходимые атрибуты для объекта RegistrationWindow."""

        self.registration_window = Tk()
        self.registration_window.title("Регистрация")
        self.registration_window.geometry('450x230')
        self.registration_window.resizable(False, False)

        self.username_label = Label(self.registration_window, text='Имя', font=font_header, justify=CENTER,
                                    **header_padding)
        self.username_label.pack()

        self.username_entry = Entry(self.registration_window, bg='#fff', fg='#444', font=font_entry)
        self.username_entry.pack()

        self.password_label = Label(self.registration_window, text='Пароль', font=font_header, justify=CENTER,
                                    **header_padding)
        self.password_label.pack()

        self.password_entry = Entry(self.registration_window, bg='#fff', fg='#444', font=font_entry)
        self.password_entry.pack()

        self.send_btn = Button(self.registration_window, text='Зарегистрироваться', command=self._send_btn_click)
        self.send_btn.pack(**base_padding)

    def _send_btn_click(self):
        """Обработчик нажатия кнопки send_btn - проверяет имя пользователя и пароль."""
        input_name = self.username_entry.get()
        input_password = self.password_entry.get()

        if not Validation.validate_user_name(username=input_name):
            messagebox.showwarning(
                title="Предупреждение",
                message="Введённое имя некорректно! Длина имени не меньше 2 символов. Разрешены только буквы.")
            return

        if len(input_password) == 0:
            messagebox.showwarning(
                title="Предупреждение",
                message="Введите пароль!"
            )
            return

        user = User(name=input_name, password=input_password)

        FileProvider.save_user(user)
        messagebox.showinfo(title="Инфо", message="Вы успешно зарегистрированы.")

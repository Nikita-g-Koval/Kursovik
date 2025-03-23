from tkinter import *
from tkinter import messagebox
from validation import Validation
from fileProvider import FileProvider
from user import User
from menu_window import MenuWindow
from registration_window import RegistrationWindow
import os

font_header = ('Arial', 15)
font_entry = ('Arial', 12)
lable_font = ('Arial', 11)
base_padding = {'padx': 10, 'pady': 8}
header_padding = {'padx': 10, 'pady': 12}


class AuthorisationWindow:
    """Класс AuthorisationWindow - инициализирует окно авторизации пользователя."""
    def __init__(self):
        """Устанавливает все необходимые атрибуты для объекта AuthorisationWindow."""
        self._create_tests_folder()

        self.main_window = Tk()
        self.main_window.title("Авторизация")
        self.main_window.geometry('450x230')
        self.main_window.resizable(False, False)

        self.username_label = Label(self.main_window, text='Имя', font=font_header, justify=CENTER,
                                    **header_padding)
        self.username_label.pack()

        self.username_entry = Entry(self.main_window, bg='#fff', fg='#444', font=font_entry)
        self.username_entry.pack()

        self.password_label = Label(self.main_window, text='Пароль', font=font_header, justify=CENTER,
                                    **header_padding)
        self.password_label.pack()

        self.password_entry = Entry(self.main_window, bg='#fff', fg='#444', font=font_entry)
        self.password_entry.pack()

        self.send_btn = Button(self.main_window, text='Перейти в меню', command=self._send_btn_click)
        self.send_btn.pack(**base_padding)

        self.registration_btn = Button(self.main_window, text='Зарегистрироваться', command=self._registration_btn_click)
        self.registration_btn.pack(**base_padding)

        self.main_window.mainloop()

    def _send_btn_click(self):
        """Обработчик нажатия кнопки send_btn - проверяет имя пользователя, если оно корректно, запускает окно Меню."""
        input_name = self.username_entry.get()
        input_password = self.password_entry.get()

        users = FileProvider.get_users()

        for old_user in users:
            if input_name == old_user.name and input_password == old_user.password:
                user = User(input_name, input_password)
                self.main_window.withdraw()
                MenuWindow(user)
                return

        messagebox.showinfo(title="Неверный ввод", message="Имя пользователя или пароль неверны.")



    @staticmethod
    def _registration_btn_click():
        RegistrationWindow()

    @staticmethod
    def _create_tests_folder():
        """Создаёт папку Tests для хранения тестов, если таковой нет."""
        if os.path.exists('Tests'):
            return

        os.mkdir('Tests')


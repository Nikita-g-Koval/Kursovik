from tkinter import *
from tkinter import messagebox
from fileProvider import FileProvider
from user import User
from menu_window import MenuWindow
from registration_window import RegistrationWindow
from window import Window
import os
import customtkinter


class AuthorisationWindow(Window):
    """Класс AuthorisationWindow - инициализирует окно авторизации пользователя."""
    def __init__(self):
        """Устанавливает все необходимые атрибуты для объекта AuthorisationWindow."""
        super().__init__()

        self.width = 340
        self.height = 280
        self.title("Авторизация")
        self.resizable(False, False)

        self._place()

        self.grid_columnconfigure(0, weight=1)

        # Создание рамки для строк ввода
        self.inputs_frame = customtkinter.CTkFrame(self)
        self.inputs_frame.grid(row=0, column=0, padx=10, pady=(10,0), sticky="nsw")

        self.username_label = customtkinter.CTkLabel(self.inputs_frame, text='Имя', justify=CENTER)
        self.username_label.grid(row=0, column=0, padx=10, pady=(0,10), sticky="w")

        self.username_entry = customtkinter.CTkEntry(self.inputs_frame, width=300)
        self.username_entry.grid(row=1, column=0, padx=10, pady=(0,10), sticky="w")

        self.password_label = customtkinter.CTkLabel(self.inputs_frame, text='Пароль', justify=CENTER)
        self.password_label.grid(row=2, column=0, padx=10, pady=(0,10), sticky="w")

        self.password_entry = customtkinter.CTkEntry(self.inputs_frame, width=300, show='*')
        self.password_entry.grid(row=3, column=0, padx=10, pady=(0,10), sticky="w")

        # Создание рамки для кнопок
        self.buttons_frame = customtkinter.CTkFrame(self)
        self.buttons_frame.grid(row=3, column=0, padx=10, pady=(10, 10), sticky="nw")

        self.send_btn = customtkinter.CTkButton(self.buttons_frame, text='Перейти в меню', width=300, command=self._send_btn_click)
        self.send_btn.grid(row=0, column=0, padx=10, pady=(10,10), sticky="nw")

        self.registration_btn = customtkinter.CTkButton(self.buttons_frame, text='Зарегистрироваться', width=300 , command=self._registration_btn_click)
        self.registration_btn.grid(row=1, column=0, padx=10, pady=(10, 10), sticky="nw")

        self.mainloop()

    def _send_btn_click(self):
        """Обработчик нажатия кнопки send_btn - проверяет имя пользователя, если оно корректно, запускает окно Меню."""
        input_name = self.username_entry.get()
        input_password = self.password_entry.get()

        users = FileProvider.get_users()

        for old_user in users:
            if input_name == old_user.name and input_password == old_user.password:
                user = User(input_name, input_password)
                self.withdraw()
                MenuWindow(user)
                return

        messagebox.showinfo(title="Неверный ввод", message="Имя пользователя или пароль неверны.")

    def _registration_btn_click(self):
        self.withdraw()
        RegistrationWindow(self._deiconify)

    def _deiconify(self):
        self.deiconify()

    @staticmethod
    def _create_tests_folder():
        """Создаёт папку Tests для хранения тестов, если таковой нет."""
        if os.path.exists('Tests'):
            return

        os.mkdir('Tests')


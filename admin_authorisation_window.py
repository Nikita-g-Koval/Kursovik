from tkinter import *
from tkinter import messagebox
from fileProvider import FileProvider
from user import User
from window import Window
from set_password_window import SetPasswordWindow
import admin_menu_window
import user_authorisation_window
import os
import customtkinter


class AdminAuthorisationWindow(Window):
    """Класс AuthorisationWindow - инициализирует окно авторизации администратора."""
    def __init__(self):
        """Устанавливает все необходимые атрибуты для объекта AuthorisationWindow."""
        super().__init__()

        self.width = 340
        self.height = 330
        self.title("Авторизация администратора")
        self.resizable(False, False)

        self._place()

        self.grid_columnconfigure(0, weight=1)

        # Создание рамки для строк ввода
        self.inputs_frame = customtkinter.CTkFrame(self)
        self.inputs_frame.grid(row=0, column=0, padx=10, pady=(10,0), sticky="nsw")

        self.username_label = customtkinter.CTkLabel(self.inputs_frame, text='Имя', justify=CENTER)
        self.username_label.grid(row=0, column=0, padx=10, pady=(0,10), sticky="w")

        self.username_entry = customtkinter.CTkEntry(self.inputs_frame, width=300)
        self.username_entry.insert(0, 'Администратор')
        self.username_entry.configure(state=DISABLED)
        self.username_entry.grid(row=1, column=0, padx=10, pady=(0,10), sticky="w")

        self.password_label = customtkinter.CTkLabel(self.inputs_frame, text='Пароль', justify=CENTER)
        self.password_label.grid(row=2, column=0, padx=10, pady=(0,10), sticky="w")

        self.password_entry = customtkinter.CTkEntry(self.inputs_frame, width=300, show='*')
        self.password_entry.grid(row=3, column=0, padx=10, pady=(0,10), sticky="w")

        # Создание рамки для кнопок
        self.buttons_frame = customtkinter.CTkFrame(self)
        self.buttons_frame.grid(row=1, column=0, padx=10, pady=(10, 10), sticky="nw")

        self.send_btn = customtkinter.CTkButton(self.buttons_frame, text='Перейти в меню', width=300,
                                                command=self._send_btn_click)
        self.send_btn.grid(row=0, column=0, padx=10, pady=(10,10), sticky="nw")

        self.set_password_btn = customtkinter.CTkButton(self.buttons_frame, text='Изменить пароль администратора', width=300,
                                                        command=self._set_password_btn_click)
        self.set_password_btn.grid(row=1, column=0, padx=10, pady=(10, 10), sticky="nw")

        self.revert_btn = customtkinter.CTkButton(self.buttons_frame, text='Войти как пользователь', width=300,
                                                  command=self._revert_btn_click)
        self.revert_btn.grid(row=2, column=0, padx=10, pady=(10, 10), sticky="nw")


        self.mainloop()

    def _revert_btn_click(self):
        self.withdraw()
        user_authorisation_window.UserAuthorisationWindow()
        self.destroy()

    def _send_btn_click(self):
        """Обработчик нажатия кнопки send_btn - проверяет пароль администратора,
         если пароль верный, запускает окно Меню."""
        input_name = self.username_entry.get()
        input_password = self.password_entry.get()

        admin_password = FileProvider.get_admin_password()


        if input_password == admin_password:
            user = User(input_name, input_password)
            self.withdraw()
            admin_menu_window.AdminMenuWindow(user)
            return

        messagebox.showinfo(title="Неверный ввод", message="Неправильный пароль.")

    def _set_password_btn_click(self):
        self.withdraw()
        SetPasswordWindow()
        self.destroy()

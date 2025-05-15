from tkinter import *
from tkinter import messagebox
from validation import Validation
from user import User
from menu_window import MenuWindow
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
        self.main_label = Label(self.main_window, text='Авторизация', font=font_header, justify=CENTER,
                                **header_padding)
        self.main_label.pack()

        self.username_entry = Entry(self.main_window, bg='#fff', fg='#444', font=font_entry)
        self.username_entry.pack()

        self.send_btn = Button(self.main_window, text='Перейти в меню', command=self._send_btn_click)
        self.send_btn.pack(**base_padding)
        self.main_window.mainloop()

    def _send_btn_click(self):
        """Обработчик нажатия кнопки send_btn - проверяет имя пользователя, если оно корректно, запускает окно Меню."""
        input_name = self.username_entry.get()
        if not Validation.validate_user_name(username=input_name):
            messagebox.showwarning(
                title="Предупреждение",
                message="Введённое имя некорректно! Длина имени не меньше 2 символов. Разрешены только буквы.")
            return
        user = User(input_name)
        self.main_window.withdraw()
        MenuWindow(user)

    @staticmethod
    def _create_tests_folder():
        """Создаёт папку Tests для хранения тестов, если таковой нет."""
        if os.path.exists('Tests'):
            return

        os.mkdir('Tests')


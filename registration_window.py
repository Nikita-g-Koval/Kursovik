from tkinter import messagebox
from validation import Validation
from user import User
from fileProvider import FileProvider
from window import Window
import user_authorisation_window
import customtkinter


class RegistrationWindow(Window):
    """Класс RegistrationWindow - инициализирует окно регистрации пользователя."""
    def __init__(self):
        """Устанавливает все необходимые атрибуты для объекта RegistrationWindow."""
        super().__init__()

        self.width = 270
        self.height = 300
        self.title("Регистрация")
        self.resizable(False, False)

        self.users = FileProvider.get_users()

        self._place()

        # Создание рамки для строк ввода
        self.inputs_frame = customtkinter.CTkFrame(self)
        self.inputs_frame.pack(padx=10, pady=(10,0))

        self.username_label = customtkinter.CTkLabel(self.inputs_frame, text='Имя')
        self.username_label.pack(padx=10, pady=(10,0), anchor="nw")

        self.username_entry = customtkinter.CTkEntry(self.inputs_frame, width=300)
        self.username_entry.pack(padx=10, pady=(4,0), anchor="nw")

        self.password_label = customtkinter.CTkLabel(self.inputs_frame, text='Пароль')
        self.password_label.pack(padx=10, pady=(10,0), anchor="nw")

        self.password_entry = customtkinter.CTkEntry(self.inputs_frame, width=300, show='*')
        self.password_entry.pack(padx=10, pady=(4,10), anchor="nw")

        # Создание рамки для кнопок
        self.buttons_frame = customtkinter.CTkFrame(self)
        self.buttons_frame.pack(padx=10, pady=(10,10))

        self.send_btn = customtkinter.CTkButton(self.buttons_frame, text='Зарегистрироваться',
                                                height=40, width=300, command=self._send_btn_click)
        self.send_btn.pack(padx=10, pady=10)

        self.return_to_auth = customtkinter.CTkButton(self.buttons_frame, text='Вернуться к авторизации',
                                                      height=40, width=300,
                                                      command=self.return_to_auth_btn_click)
        self.return_to_auth.pack(padx=10, pady=10)

        self.mainloop()

    def _send_btn_click(self):
        """Обработчик нажатия кнопки send_btn - проверяет имя пользователя и пароль."""
        input_name = self.username_entry.get()
        input_password = self.password_entry.get()

        for user in self.users:
            if input_name == user.name or input_name == "Администратор":
                messagebox.showwarning(
                    title="Предупреждение",
                    message="Введённое имя занято.")
                return

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

    def return_to_auth_btn_click(self):
        """Обработчик нажатия кнопки return_to_auth_btn_click - возвращает пользователя в окно авторизации."""
        self.withdraw()
        user_authorisation_window.UserAuthorisationWindow()
        self.destroy()

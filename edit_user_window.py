from tkinter import messagebox
from validation import Validation
from user import User
from fileProvider import FileProvider
import customtkinter
import users_window


class EditUserWindow(customtkinter.CTkToplevel):
    """Класс EditUserWindow - инициализирует окно редактирования пользователя."""
    def __init__(self, parent_window, user: User):
        """Устанавливает все необходимые атрибуты для объекта EditUserWindow."""
        super().__init__(parent_window)

        self.parent_window = parent_window
        self.user = user
        self.users = FileProvider.get_users()

        self.width = 340
        self.height = 250
        self.title("Редактирование пользователя")
        self.resizable(False, False)

        self._place()


        # Создание рамки для строк ввода
        self.inputs_frame = customtkinter.CTkFrame(self)
        self.inputs_frame.pack(padx=10, pady=(10,0))

        self.username_label = customtkinter.CTkLabel(self.inputs_frame, text='Имя')
        self.username_label.pack(padx=10, pady=(10,0), anchor="nw")

        self.username_entry = customtkinter.CTkEntry(self.inputs_frame, width=300)
        self.username_entry.insert(0, self.user.name)
        self.username_entry.pack(padx=10, pady=(4,0), anchor="nw")

        self.password_label = customtkinter.CTkLabel(self.inputs_frame, text='Пароль')
        self.password_label.pack(padx=10, pady=(10,0), anchor="nw")

        self.password_entry = customtkinter.CTkEntry(self.inputs_frame, width=300)
        self.password_entry.insert(0, self.user.password)
        self.password_entry.pack(padx=10, pady=(4,10), anchor="nw")

        # Создание рамки для кнопок
        self.buttons_frame = customtkinter.CTkFrame(self)
        self.buttons_frame.pack(padx=10, pady=(10,10))

        self.send_btn = customtkinter.CTkButton(self.buttons_frame, text='Сохранить изменения',
                                                height=40, width=300, command=self._send_btn_click)
        self.send_btn.pack(padx=10, pady=10)

        self.grab_set()

        self.protocol("WM_DELETE_WINDOW", self._on_closing)

        self.mainloop()

    def _on_closing(self):
        self.parent_window.show_users()
        self.destroy()

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
                message="Введённое имя некорректно! Длина имени не меньше 2 символов.")
            return

        if len(input_password) == 0:
            messagebox.showwarning(
                title="Предупреждение",
                message="Введите пароль!"
            )
            return

        user = User(name=input_name, password=input_password)

        FileProvider.delete_user(self.user.name)
        FileProvider.save_user(user)
        messagebox.showinfo(title="Инфо", message="Данные успешно изменены.")

    def _place(self):
        # get screen width and height
        ws = self.winfo_screenwidth()  # width of the screen
        hs = self.winfo_screenheight()  # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = (ws / 2) - (self.width / 2)
        y = (hs / 2) - (self.height / 2)

        # set the dimensions of the screen
        # and where it is placed
        self.geometry('%dx%d+%d+%d' % (self.width, self.height, x, y))

from tkinter import ttk, messagebox
from fileProvider import FileProvider
import admin_authorisation_window
import customtkinter


class SetPasswordWindow(customtkinter.CTk):
    """Класс MenuWindow - инициализирует окно результатов тестов."""
    def __init__(self):
        """Устанавливает все необходимые атрибуты для объекта ResultsWindow."""

        super().__init__()

        self.title("Изменение пароля")
        self.width = 350
        self.height = 385
        self.resizable(False, False)
        self.configure(padx=20, pady=20)

        self._place()

        # Создание рамки для строк ввода
        self.inputs_frame = customtkinter.CTkFrame(self)
        self.inputs_frame.pack()

        customtkinter.CTkLabel(self.inputs_frame, text='Старый пароль').pack(padx=10, pady=(10, 0), anchor="nw")

        self.old_password_entry = customtkinter.CTkEntry(self.inputs_frame, width=300, show='*')
        self.old_password_entry.pack(padx=10, pady=(4, 0), anchor="nw")

        customtkinter.CTkLabel(self.inputs_frame, text='Новый пароль').pack(padx=10, pady=(10, 0), anchor="nw")

        self.new_password_entry = customtkinter.CTkEntry(self.inputs_frame, width=300, show='*')
        self.new_password_entry.pack(padx=10, pady=(4, 10), anchor="nw")

        (customtkinter.CTkLabel(self.inputs_frame, text='Повторный ввод нового пароля')
         .pack(padx=10, pady=(10, 0), anchor="nw"))

        self.new_password_re_entry = customtkinter.CTkEntry(self.inputs_frame, width=300, show='*')
        self.new_password_re_entry.pack(padx=10, pady=(4, 10), anchor="nw")

        # Создание рамки для кнопок
        self.buttons_frame = customtkinter.CTkFrame(self)
        self.buttons_frame.pack()

        self.send_btn = customtkinter.CTkButton(self.buttons_frame, text='Изменить пароль', height=40, width=300,
                                                command=self._send_btn_click)
        self.send_btn.pack(padx=10, pady=10)

        self.return_to_auth = customtkinter.CTkButton(self.buttons_frame, text='Назад', height=40, width=300,
                                                      command=self.return_to_auth_btn_click)
        self.return_to_auth.pack(padx=10, pady=10)

        self.protocol("WM_DELETE_WINDOW", self.return_to_auth_btn_click)


        self.mainloop()

    def _send_btn_click(self):
        """Обработчик нажатия кнопки send_btn - проверяет имя пользователя и пароль."""
        input_old_password = self.old_password_entry.get()
        input_new_password = self.new_password_entry.get()
        reinput_new_password = self.new_password_re_entry.get()

        admin_password = FileProvider.get_admin_password()

        if input_old_password != admin_password:
            messagebox.showwarning(
                title="Предупреждение",
                message="Неправильный текущий пароль."
            )
            return

        if input_new_password == input_old_password:
            messagebox.showwarning(
                title="Предупреждение",
                message="Новый и текущий пароли совпадают."
            )
            return

        if input_new_password != reinput_new_password:
            messagebox.showwarning(
                title="Предупреждение",
                message="Повторный ввод нового пароля не совпадает с его первым вводом."
            )
            return

        FileProvider.set_admin_password(input_new_password)

        messagebox.showinfo(title="Инфо", message="Пароль успешно изменён.")

    def return_to_auth_btn_click(self):
        """Обработчик нажатия кнопки return_to_auth_btn_click - возвращает пользователя в окно авторизации."""
        self.withdraw()
        admin_authorisation_window.AdminAuthorisationWindow()
        self.destroy()



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
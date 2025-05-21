from tkinter import *
from tkinter import ttk
from create_user_window import CreateUserWindow
from edit_user_window import EditUserWindow
from tkinter import messagebox
import admin_menu_window
from fileProvider import FileProvider
from user import User
from window import Window
import customtkinter


class UsersWindow(Window):
    """Класс UsersWindow - инициализирует окно пользователей."""
    def __init__(self, user: User):
        """Устанавливает все необходимые атрибуты для объекта UsersWindow."""
        super().__init__()

        self.user = user
        self.selected_item = None

        self.title("Управление пользователями")
        self.width = 640
        self.height = 400
        self.resizable(True, True)

        self._place()

        # Создание рамки для кнопок
        self.buttons_frame = customtkinter.CTkFrame(self)
        self.buttons_frame.pack()

        self.add_user_btn = customtkinter.CTkButton(self.buttons_frame, text='Добавить пользователя',
                                                       command=self._add_user_btn_click)
        self.add_user_btn.grid(row=0, column=0, padx=10, pady=10)

        self.edit_user_btn = customtkinter.CTkButton(self.buttons_frame, text='Редактировать',
                                                       command=self._edit_user_btn_click)
        self.edit_user_btn.grid(row=0, column=1, padx=(0,10), pady=10)

        self.delete_user_btn = customtkinter.CTkButton(self.buttons_frame, text='Удалить',
                                                        command=self._delete_user_btn_click)
        self.delete_user_btn.grid(row=0, column=2, padx=(0,10), pady=10)

        self.back_to_menu_btn = customtkinter.CTkButton(self.buttons_frame, text='Вернуться в меню',
                                                        command=self.back_to_menu_btn_click)
        self.back_to_menu_btn.grid(row=0, column=3, padx=(0,10), pady=10)


        self.columns = "name"

        self.users_tree = ttk.Treeview(self, columns=self.columns, show="headings")
        self.users_tree.pack(expand=True, fill=BOTH, padx=10, pady=(0, 10))


        self.users_tree.heading("name", text="Имя", anchor=W)

        self.users_tree.column("#1", stretch=YES, width=200)


        self.show_users()

        self.scrollbar = ttk.Scrollbar(self, orient=VERTICAL, command=self.users_tree.yview)
        self.users_tree.configure(yscrollcommand=self.scrollbar.set)
        self.users_tree.bind("<<TreeviewSelect>>", self.on_click)
        self.users_tree.pack()

        self.mainloop()

    def on_click(self, event):
        item_tuple = self.users_tree.selection()
        if len(item_tuple) > 0:
            self.selected_item = item_tuple[0]


    def _add_user_btn_click(self):
        CreateUserWindow(self)

    def _edit_user_btn_click(self):
        if self.selected_item is not None:
            selected_user_name = self.users_tree.item(self.selected_item, "values")[0]
            users = FileProvider.get_users()
            selected_user = None
            for user in users:
                if user.name == selected_user_name:
                    selected_user = user
                    break

            EditUserWindow(parent_window=self, user=selected_user)

            self.show_users()
            self.selected_item = None

        else:
            messagebox.showwarning(title="Предупреждение", message="Выберите строку с нужным пользователем.")

    def _delete_user_btn_click(self):
        if self.selected_item is not None:
            user_name = self.users_tree.item(self.selected_item, "values")[0]
            FileProvider.delete_user(user_name)

            self.show_users()
            self.selected_item = None
            messagebox.showinfo(title="Инфо", message="Пользователь успешно удалён.")
        else:
            messagebox.showwarning(title="Предупреждение", message="Выберите строку с нужным пользователем.")


    def back_to_menu_btn_click(self):
        """Обработчик нажатия кнопки back_to_menu_btn - удаляет данное окно и создаёт объект MenuWindow."""
        self.withdraw()
        admin_menu_window.AdminMenuWindow(self.user)
        self.destroy()

    def show_users(self):
        users = FileProvider.get_users()

        self.users_tree.delete(*self.users_tree.get_children())

        for user in users:
            self.users_tree.insert("", END, values=(user.name,))

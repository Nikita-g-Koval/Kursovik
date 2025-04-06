from tkinter import *
from tkinter import messagebox
from questionsStrorage import QuestionsStorage
from fileProvider import FileProvider
from user import User
from window import Window
import menu_window
import customtkinter


class DeleteQuestionWindow(Window):
    """Класс DeleteQuestionWindow - инициализирует окно для удаления вопроса."""
    def __init__(self, questions_storage: QuestionsStorage, user: User):
        """Устанавливает все необходимые атрибуты для объекта DeleteQuestionWindow."""
        super().__init__()

        self.questions_storage = questions_storage
        self.user = user

        self.title('Удаление вопроса')
        self.width = 600
        self.height = 350
        self.resizable(True, True)

        self._place()

        self.grid_columnconfigure(0, weight=1)

        # Создание рамки для текстбокса
        self.textbox_frame = customtkinter.CTkFrame(self)
        self.textbox_frame.grid_columnconfigure(0, weight=1)
        self.textbox_frame.grid(row=0, column=0, padx=10, pady=(10, 10), sticky="nsew", columnspan=2)

        # Создание рамки для строк ввода
        self.inputs_frame = customtkinter.CTkFrame(self)
        self.inputs_frame.grid_columnconfigure(1, weight=1)
        self.inputs_frame.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="nsew", columnspan=2)

        self.questions_editor = customtkinter.CTkTextbox(self.textbox_frame, wrap="word")
        self.questions_editor.grid(row=0, column=0, padx=10, pady=(10, 10), sticky="nsew")

        self._print_questions()

        self.questionNumber_entry = customtkinter.CTkEntry(self.inputs_frame)
        self.questionNumber_entry.grid(row=0, column=0, padx=10, pady=(10, 10), sticky="nsew")

        self.delete_question_btn = customtkinter.CTkButton(self.inputs_frame,
                                          text='Удалить вопрос', command=self._delete_question_btn_click)
        self.delete_question_btn.grid(row=0, column=1, padx=(0, 10), pady=(10, 10), sticky=E)

        self.save_changes_btn = customtkinter.CTkButton(self.inputs_frame,
                                       text='Сохранить изменения', command=self._save_changes_btn_click)
        self.save_changes_btn.grid(row=0, column=2, padx=(0, 10), pady=(10, 10), sticky=E)

        self.back_to_menu_btn = customtkinter.CTkButton(self, text='Вернуться в меню',
                                                        command=self.back_to_menu_btn_click, width=70)
        self.back_to_menu_btn.grid(row=2, column=1, padx=10, pady=10)


        self.mainloop()

    def _delete_question_btn_click(self):
        """Обработчик нажатия кнопки delete_question_btn - удаляет вопрос по введённому пользователем индексу."""
        question_number = self.questionNumber_entry.get()
        if not question_number.isdigit():
            messagebox.showwarning(title="Предупреждение", message="Введите номер вопроса, целое число.")
            return
        number = int(question_number)

        if number < 1 or number > len(self.questions_storage.test.questions):
            messagebox.showwarning(title="Предупреждение",
                                   message="Номер вопроса выходит за границу количества вопросов.")
            return

        self.questions_storage.remove_question(number)
        self._print_questions()
        messagebox.showinfo(title="Уведомление", message="Вопрос успешно удалён. Сохраните изменения.")

    def _save_changes_btn_click(self):
        """Обработчик нажатия кнопки save_changes_btn - сохраняет текущие вопросы, ничего не возвращает."""
        FileProvider.save_test_changes(self.questions_storage.test, self.questions_storage.test_path)
        messagebox.showinfo(title="Уведомление", message="Изменения сохранены.")

    def _print_questions(self):
        """Отображает текущие вопросы."""
        self.questions_editor.delete('1.0', END)
        questions = self.questions_storage.test.questions
        count = 1
        for q in questions:
            self.questions_editor.insert(END, "№{i} {question}\n".format(i=count, question=q.text))
            count += 1

    def back_to_menu_btn_click(self):
        """Обработчик нажатия кнопки back_to_menu_btn - удаляет данное окно и создаёт объект MenuWindow."""
        self.withdraw()
        menu_window.MenuWindow(self.user)
        self.destroy()

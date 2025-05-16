from tkinter import *
from tkinter import messagebox
from questionsStorage import QuestionsStorage
from validation import Validation
from fileProvider import FileProvider
from question import Question
from answer import Answer
from user import User
from window import Window
import addQuestion_window
import admin_menu_window
import customtkinter


class AddBaseQuestionWindow(Window):
    """Класс AddBaseQuestionWindow - инициализирует окно для добавления базового вопроса."""
    def __init__(self, questions_storage: QuestionsStorage, user: User):
        """Устанавливает все необходимые атрибуты для объекта AddBaseQuestionWindow."""
        super().__init__()

        self.questions_storage = questions_storage
        self.user = user

        self.width = 540
        self.height = 380
        self.title('Добавление вопроса')
        self.resizable(False, True)

        self._place()

        self.grid_columnconfigure(0, weight=1)


        # Создание рамки для строк ввода
        self.inputs_frame = customtkinter.CTkFrame(self)
        self.inputs_frame.grid(row=0, column=0, padx=10, pady=(10, 0), columnspan=2)

        customtkinter.CTkLabel(self.inputs_frame, text="Текст вопроса:").grid(row=0, column=0, padx=10,
                                                                              pady=(10, 0), sticky="nw")
        self.questionText_entry = customtkinter.CTkEntry(self.inputs_frame, height=70, width=500)
        self.questionText_entry.grid(row=1, column=0, padx=10, pady=(10, 10), sticky="nw")

        customtkinter.CTkLabel(self.inputs_frame, text="Ответ на вопрос:").grid(row=2, column=0, padx=10,
                                                                                pady=(10, 0), sticky="nw")
        self.answer_entry = customtkinter.CTkEntry(self.inputs_frame, height=70, width=500)
        self.answer_entry.grid(row=3, column=0, padx=10, pady=(10, 10), sticky="nw")


        # Создание рамки для кнопок добавления вопроса
        self.buttons_frame = customtkinter.CTkFrame(self)
        self.buttons_frame.grid(row=1, column=0, padx=10, pady=(10, 10), sticky=NW)

        self.add_question_btn = customtkinter.CTkButton(self.buttons_frame, text="Добавить вопрос",
                                       command=self._add_question_btn_click, height=66)
        self.add_question_btn.grid(row=0, column=0, padx=10, pady=(10, 10))

        self.save_changes_btn = customtkinter.CTkButton(self.buttons_frame, text="Сохранить изменения",
                                       command=self._save_changes_btn_click, height=66)
        self.save_changes_btn.grid(row=0, column=1, padx=(0,10), pady=(10, 10))


        # Создание рамки для кнопок возврата в меню или назад
        self.return_buttons_frame = customtkinter.CTkFrame(self)
        self.return_buttons_frame.grid(row=1, column=1, padx=10, pady=(10, 10))

        self.back_to_menu_btn = customtkinter.CTkButton(self.return_buttons_frame, text='Назад',
                                                        command=self.return_btn_click)
        self.back_to_menu_btn.grid(row=0, column=0, padx=10, pady=(10, 10))

        self.back_to_menu_btn = customtkinter.CTkButton(self.return_buttons_frame, text='Вернуться в меню',
                                                        command=self.back_to_menu_btn_click)
        self.back_to_menu_btn.grid(row=1, column=0, padx=10, pady=(0, 10))

        self._place()


        self.mainloop()

    def _add_question_btn_click(self):
        """Обработчик нажатия кнопки add_question_btn - добавляет новый вопрос, ничего не возвращает."""
        input_question = self.questionText_entry.get()
        input_answer = self.answer_entry.get()

        if not Validation.validate_question(input_question):
            messagebox.showwarning(title="Предупреждение", message="Длина вопроса должна быть > 0 и < 120.")
            return

        if not Validation.validate_answer(input_answer):
            messagebox.showwarning(title="Предупреждение", message="Не был введён ответ.")
            return

        answers = [Answer(input_answer, True)]
        question = Question(input_question, answers)

        self.questions_storage.add_question(question)
        messagebox.showinfo(title="Оповещение", message="Вопрос успешно добавлен. Сохраните изменения.")

    def _save_changes_btn_click(self):
        """Обработчик нажатия кнопки save_changes_btn - сохраняет текущие вопросы, ничего не возвращает."""
        FileProvider.save_test_changes(self.questions_storage.test, self.questions_storage.test_path)
        messagebox.showinfo(title="Оповещение", message="Изменения сохранены.")

    def return_btn_click(self):
        """Обработчик нажатия кнопки back_to_menu_btn - удаляет данное окно и создаёт объект MenuWindow."""
        self.withdraw()
        addQuestion_window.AddQuestionWindow(self.questions_storage, self.user)
        self.destroy()

    def back_to_menu_btn_click(self):
        """Обработчик нажатия кнопки back_to_menu_btn - удаляет данное окно и создаёт объект MenuWindow."""
        self.withdraw()
        admin_menu_window.AdminMenuWindow(self.user)
        self.destroy()

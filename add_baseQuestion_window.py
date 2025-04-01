from tkinter import *
from tkinter import messagebox
from questionsStrorage import QuestionsStorage
from validation import Validation
from fileProvider import FileProvider
from question import Question
from answer import Answer
import customtkinter


# Настройка внешнего вида и темы GUI-окна
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")


class AddBaseQuestionWindow(customtkinter.CTk):
    """Класс AddBaseQuestionWindow - инициализирует окно для добавления базового вопроса."""
    def __init__(self, questions_storage: QuestionsStorage):
        """Устанавливает все необходимые атрибуты для объекта AddBaseQuestionWindow."""
        super().__init__()

        self.questions_storage = questions_storage
        self.title('Добавление вопроса')
        self.geometry('540x350')
        self.resizable(False, True)

        self.grid_columnconfigure(0, weight=1)

        # Создание рамки для строк ввода
        self.inputs_frame = customtkinter.CTkFrame(self)
        self.inputs_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsw")

        # Создание рамки для кнопок
        self.buttons_frame = customtkinter.CTkFrame(self)
        self.buttons_frame.grid(row=1, column=0, padx=10, pady=(10, 10), sticky="nsw")

        customtkinter.CTkLabel(self.inputs_frame, text="Текст вопроса:").grid(row=0, column=0, padx=10,
                                                                              pady=(10, 0), sticky="nw")
        self.questionText_entry = customtkinter.CTkEntry(self.inputs_frame, height=70, width=500)
        self.questionText_entry.grid(row=1, column=0, padx=10, pady=(10, 10), sticky="nw")

        customtkinter.CTkLabel(self.inputs_frame, text="Ответ на вопрос:").grid(row=2, column=0, padx=10,
                                                                                pady=(10, 0), sticky="nw")
        self.answer_entry = customtkinter.CTkEntry(self.inputs_frame, height=70, width=500)
        self.answer_entry.grid(row=3, column=0, padx=10, pady=(10, 10), sticky="nw")

        self.add_question_btn = customtkinter.CTkButton(self.buttons_frame, text="Добавить вопрос",
                                       command=self._add_question_btn_click, height=40)
        self.add_question_btn.grid(row=0, column=0, padx=10, pady=(10, 10))

        self.save_changes_btn = customtkinter.CTkButton(self.buttons_frame, text="Сохранить изменения",
                                       command=self._save_changes_btn_click, height=40)
        self.save_changes_btn.grid(row=0, column=1, padx=(0,10), pady=(10, 10))

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

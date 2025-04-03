from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
from question_type import QuestionType
from test_result import TestResult
from answer import Answer
from user import User
from fileProvider import FileProvider
from questionsStrorage import QuestionsStorage
from typing import List
from test import Test
import customtkinter


# Настройка внешнего вида и темы GUI-окна
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")


class TestWindow(customtkinter.CTk):
    """Класс TestWindow - инициализирует окно теста."""
    def __init__(self, user: User, questions_storage: QuestionsStorage, test_name: str):
        """Устанавливает все необходимые атрибуты для объекта TestWindow."""
        super().__init__()
        self.user = user
        self.rightAnswersCount = 0
        self.test_result = None

        self.qs = questions_storage
        self.title("Тест")
        self.geometry('800x400')
        self.resizable(True, True)

        self.test = self.qs.test
        self.test.start_test()

        # Создание рамки для вопросов
        self.inputs_frame = customtkinter.CTkFrame(self)
        self.inputs_frame.pack(padx=10, pady=(10, 10))

        # Создание рамки для кнопок
        self.buttons_frame = customtkinter.CTkFrame(self)
        self.buttons_frame.pack(padx=10, pady=(0, 10))

        self.test_label = customtkinter.CTkLabel(self.inputs_frame, justify=CENTER)
        self.test_label.pack()

        self.selected_id = IntVar(self)
        self.answer_entry = Entry(self)
        self.radio_buttons = []
        self.check_buttons = []
        self.selected_buttons = []

        self.save_results_btn = customtkinter.CTkButton(self.buttons_frame, text='Сохранить результаты',
                                       command=self._save_results_btn_click)
        self.save_results_btn.pack(padx=10, pady=10, side=BOTTOM)

        self.acceptAnswer_btn = customtkinter.CTkButton(self.buttons_frame, text='Ответить', command=self._accept_answer_btn_clicked)
        self.acceptAnswer_btn.pack(padx=10, pady=10, side=BOTTOM)

        self._show_next_question()

        self.mainloop()

    def _save_results_btn_click(self):
        """Обработчик нажатия кнопки save_results_btn - сохраняет результаты теста."""
        if self.test_result is None:
            messagebox.showwarning(title="Предупреждение", message="Сначала пройдите тест!")
            return

        FileProvider.save_test_result(self.test_result)
        messagebox.showinfo(title="Сообщение", message="Результаты успешно сохранены.")

    def _show_answers(self):
        """Отображает ответы на текущий вопрос."""
        self._clear_answers()

        match self.test.get_current_question.get_type:
            case QuestionType.base:
                self.answer_entry = customtkinter.CTkEntry(self.inputs_frame)
                self.answer_entry.pack(padx=10, pady=10)
            case QuestionType.radio_button:
                self._init_radiobuttons()
            case QuestionType.check_button:
                self._init_checkbuttons()

    def _get_answer_from_radiobutton(self):
        """Возвращает выбранный ответ из radiobuttons."""
        answer: Answer = self.test.get_current_answers[self.selected_id.get()]
        return answer

    def _accept_answer_btn_clicked(self):
        """Принимает ответ пользователя и начисляет ему соответствующее количество очков."""
        user_answers: List[Answer] = []
        match self.test.get_current_question.get_type:
            case QuestionType.base:
                answer = Answer(text=self.answer_entry.get())
                user_answers.append(answer)
            case QuestionType.radio_button:
                answer = self._get_answer_from_radiobutton()
                user_answers.append(answer)
            case QuestionType.check_button:
                for btn in self.selected_buttons:
                    if btn.get() >= len(self.test.get_current_answers):
                        continue
                    answer = self.test.get_current_answers[btn.get()]
                    user_answers.append(answer)

        self.test.accept_answers(user_answers)

        self.test.next_question()

        if self.test.is_finished:
            right_answers_percentage = self.test.summarise()
            self.test_result = TestResult(self.user.name, self.test.score, right_answers_percentage, datetime.now())

            self.acceptAnswer_btn.configure(state=DISABLED)

            messagebox.showinfo(title="Тест завершён",
                                message="{0}, процент правильных ответов: {1}".format(self.user.name,
                                                                                              right_answers_percentage))
            return

        self._show_next_question()

    def _show_next_question(self):
        """Отображает следующий вопрос."""
        self.test_label.configure(text=self.test.print_current_question())
        self._show_answers()

    def _init_radiobuttons(self):
        """Инициализирует radiobuttons."""
        self.selected_id.set(0)

        for i in range(len(self.test.get_current_answers)):
            answer_btn = customtkinter.CTkRadioButton(self.inputs_frame, text=self.test.get_current_answers[i].text, value=i,
                                         variable=self.selected_id)
            answer_btn.pack(padx=10, pady=10)
            self.radio_buttons.append(answer_btn)

    def _init_checkbuttons(self):
        """Инициализирует checkbuttons."""
        for i in range(len(self.test.get_current_answers)):
            selected_id = IntVar(self)
            selected_id.set(len(self.test.get_current_answers) + 1)
            self.selected_buttons.append(selected_id)

            answer_btn = customtkinter.CTkCheckBox(self.inputs_frame, text=self.test.get_current_answers[i].text,
                                         offvalue=len(self.test.get_current_answers) + 1,
                                         onvalue=i,
                                         variable=selected_id)
            answer_btn.pack(padx=10, pady=10)
            self.check_buttons.append(answer_btn)

    def _clear_answers(self):
        """Очищает все инициализированные кнопки ответов."""
        self.answer_entry.destroy()
        for btn in self.radio_buttons:
            btn.destroy()

        for btn in self.check_buttons:
            btn.destroy()

        self.radio_buttons.clear()
        self.check_buttons.clear()
        self.selected_buttons.clear()

from tkinter import *
from tkinter import messagebox
from typing import List
import addQuestion_window
import admin_menu_window
from questionsStorage import QuestionsStorage
from validation import Validation
from fileProvider import FileProvider
from question import Question
from answer import Answer
from question_checkButton import QuestionCheckButton
from user import User
from window import Window
import customtkinter


class AddCheckButtonQuestion(Window):
    """Класс AddCheckButtonQuestion - инициализирует окно для добавления вопроса с множественным выбором."""
    new_question: Question

    def __init__(self, questions_storage: QuestionsStorage, user: User):
        """Устанавливает все необходимые атрибуты для объекта AddCheckButtonQuestion."""
        super().__init__()
        self.answers: List[Answer] = []
        self.questions_storage = questions_storage
        self.user = user

        self.width = 800
        self.height = 420
        self.title('Добавление вопроса с множественным выбором')
        self.resizable(False, True)

        self._place()

        self.check_buttons = []
        self.selections: List[IntVar] = []

        self.selected_true = BooleanVar(self)
        self.selected_true.set(False)

        self.grid_columnconfigure(1, weight=1)

        # Создание рамки для чекбоксов ответов
        self.checkboxes_frame = customtkinter.CTkFrame(self)
        self.checkboxes_frame.grid(row=0, column=1, padx=(10, 10), pady=(10, 0), sticky=NSEW)

        # Создание рамки для строк ввода
        self.inputs_frame = customtkinter.CTkFrame(self)
        self.inputs_frame.grid(row=0, column=0, padx=(10,0), pady=(10, 0), sticky="nsw")

        customtkinter.CTkLabel(self.inputs_frame, text="Текст вопроса:", justify=LEFT).grid(row=0, column=0, sticky=W,
                                                                                            padx=10, pady=(10,0))
        self.questionText_entry = customtkinter.CTkEntry(self.inputs_frame, height=70, width=500, justify=LEFT)
        self.questionText_entry.grid(row=1, column=0, sticky=EW, padx=10, pady=(10, 0))

        customtkinter.CTkLabel(self.inputs_frame, text="Ответ на вопрос:", justify=LEFT).grid(row=2, column=0, sticky=W,
                                                                             padx=10, pady=(10,0))
        self.answer_entry = customtkinter.CTkEntry(self.inputs_frame, height=70, width=500, justify=LEFT)
        self.answer_entry.grid(row=3, column=0, sticky=EW, padx=10, pady=(10, 0))

        self.answer_is_correct_checkBtn = customtkinter.CTkCheckBox(self.inputs_frame,
                                                      text="Ответ верный",
                                                      variable=self.selected_true)
        self.answer_is_correct_checkBtn.grid(row=4, column=0, sticky=EW, padx=10, pady=(10, 10))


        # Создание рамки для кнопок добавления ответов
        self.buttons_a_frame = customtkinter.CTkFrame(self)
        self.buttons_a_frame.grid(row=1, column=0, padx=10, pady=(10, 10), sticky="nsw")

        self.add_answer_btn = customtkinter.CTkButton(self.buttons_a_frame, text="Добавить ответ",
                                     command=self._add_answer_btn_click, width=160)
        self.add_answer_btn.grid(row=0, column=0, padx=(10, 0), pady=10, sticky="nsw")

        self.remove_answer_btn = customtkinter.CTkButton(self.buttons_a_frame, text="Удалить ответ",
                                        command=self._remove_answer_btn_click, width=160)
        self.remove_answer_btn.grid(row=0, column=1, padx=(10,10), pady=10)


        # Создание рамки для кнопок вопроса
        self.buttons_q_frame = customtkinter.CTkFrame(self)
        self.buttons_q_frame.grid(row=2, column=0, padx=10, pady=(0, 10), sticky="nsw")

        self.add_question_btn = customtkinter.CTkButton(self.buttons_q_frame, text="Добавить вопрос",
                                       command=self._add_question_btn_click, width=160)
        self.add_question_btn.grid(row=0, column=0, padx=(10,0), pady=10)

        self.save_changes_btn = customtkinter.CTkButton(self.buttons_q_frame, text="Сохранить изменения",
                                       command=self._save_changes_btn_click, width=160)
        self.save_changes_btn.grid(row=0, column=1, padx=10, pady=10)


        # Создание рамки для кнопок возврата в меню или назад
        self.return_buttons_frame = customtkinter.CTkFrame(self)
        self.return_buttons_frame.grid(row=1, column=1, padx=10, pady=(10, 10), rowspan=2, sticky="se")

        self.back_to_menu_btn = customtkinter.CTkButton(self.return_buttons_frame, text='Назад',
                                                        command=self.return_btn_click)
        self.back_to_menu_btn.grid(row=0, column=0, padx=10, pady=(10, 10), sticky=E)

        self.back_to_menu_btn = customtkinter.CTkButton(self.return_buttons_frame, text='Вернуться в меню',
                                                        command=self.back_to_menu_btn_click)
        self.back_to_menu_btn.grid(row=1, column=0, padx=10, pady=(0, 10), sticky=E)


        self.protocol("WM_DELETE_WINDOW", self._on_closing)

        self.mainloop()

    def _add_answer_btn_click(self):
        """Обработчик нажатия кнопки add_answer_btn - добавляет новый ответ, ничего не возвращает."""
        if len(self.answers) >= 6:
            messagebox.showwarning(title="Предупреждение",
                                   message="Максимальное количество ответов 6. Больше добавить нельзя.")
            return

        input_answer = self.answer_entry.get()
        if len(input_answer) == 0:
            messagebox.showwarning(title="Предупреждение", message="Данные не были введены!")
            return

        correctness = self.selected_true.get()
        answer = Answer(input_answer, correctness)

        self.answers.append(answer)
        self._init_checkbuttons()

    def _remove_answer_btn_click(self):
        """Обработчик нажатия кнопки remove_answer_btn- удаляет выбранные пользователем ответы, ничего не возвращает."""
        if len(self.answers) > 0:
            selected_answers = []

            for select in self.selections:
                if select.get() > len(self.answers):
                    continue

                selected_answers.append(self.answers[select.get()])

            for answer in selected_answers:
                self.answers.remove(answer)

            self._init_checkbuttons()

    def _add_question_btn_click(self):
        """Обработчик нажатия кнопки add_question_btn - добавляет новый вопрос, ничего не возвращает."""
        question_text = self.questionText_entry.get()

        if not Validation.validate_question(question_text):
            messagebox.showwarning(title="Предупреждение",
                                   message="Введены некорректные данные! Введите текст вопроса.")
            return

        if len(self.answers) < 2:
            messagebox.showwarning(title="Предупреждение",
                                   message="Количество вопросов должно быть не менее двух!")
            return

        self.new_question = QuestionCheckButton(question_text, self.answers)
        self.questions_storage.add_question(self.new_question)
        messagebox.showinfo(title="Успешно", message="Вопрос добавлен.")

    def _save_changes_btn_click(self):
        """Обработчик нажатия кнопки save_changes_btn - сохраняет текущие вопросы, ничего не возвращает."""
        FileProvider.save_test_changes(self.questions_storage.test, self.questions_storage.test_path)
        messagebox.showinfo(title="Успешно", message="Изменения сохранены.")

    def _init_checkbuttons(self):
        """Инициализирует checkbuttons в соответствии с вопросами, ничего не возвращает."""
        self._clear_checkbuttons()

        for i in range(len(self.answers)):
            selected_id = IntVar(self)
            selected_id.set(len(self.answers) + 1)
            self.selections.append(selected_id)

            answer_btn = customtkinter.CTkCheckBox(self.checkboxes_frame, text=self.answers[i].text,
                                                   offvalue=len(self.answers) + 1,
                                                   onvalue=i,
                                                   variable=selected_id,
                                                   )

            if self.answers[i].is_correct:
                answer_btn.configure(text_color="green")

            answer_btn.pack(padx=10, pady=10, anchor=W)
            self.check_buttons.append(answer_btn)

    def _clear_checkbuttons(self):
        """Удаляет все инициализированные checkbuttons, ничего не возвращает."""
        for btn in self.check_buttons:
            btn.destroy()
        self.check_buttons.clear()
        self.selections.clear()


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

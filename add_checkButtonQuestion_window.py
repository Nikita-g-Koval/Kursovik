from tkinter import *
from tkinter import messagebox
from typing import List
from questionsStrorage import QuestionsStorage
from validation import Validation
from fileProvider import FileProvider
from question import Question
from answer import Answer
from question_checkButton import QuestionCheckButton


class AddCheckButtonQuestion:
    """Класс AddCheckButtonQuestion - инициализирует окно для добавления вопроса с множественным выбором."""
    new_question: Question

    def __init__(self, questions_storage: QuestionsStorage):
        """Устанавливает все необходимые атрибуты для объекта AddCheckButtonQuestion."""
        self.answers: List[Answer] = []
        self.questions_storage = questions_storage
        self.add_checkButtonQuestion_window = Tk()
        self.add_checkButtonQuestion_window.title('Добавление вопроса с множественным выбором')
        self.add_checkButtonQuestion_window.geometry('900x200')
        self.add_checkButtonQuestion_window.resizable(False, True)
        self.check_buttons = []
        self.selections: List[IntVar] = []

        self.selected_true = BooleanVar(self.add_checkButtonQuestion_window)
        self.selected_true.set(False)

        Label(self.add_checkButtonQuestion_window, text="Текст вопроса:", justify=LEFT).grid(row=0, column=0, sticky=W)
        self.questionText_entry = Entry(self.add_checkButtonQuestion_window, width=30)
        self.questionText_entry.grid(row=0, column=1, sticky=EW)

        Label(self.add_checkButtonQuestion_window, text="Ответ на вопрос:",
              justify=LEFT).grid(row=1, column=0, sticky=W)
        self.answer_entry = Entry(self.add_checkButtonQuestion_window, width=30)
        self.answer_entry.grid(row=1, column=1, sticky=EW)

        self.answer_is_correct_checkBtn = Checkbutton(self.add_checkButtonQuestion_window,
                                                      text="Ответ верный",
                                                      variable=self.selected_true)
        self.answer_is_correct_checkBtn.grid(row=1, column=2)

        self.add_answer_btn = Button(self.add_checkButtonQuestion_window, text="Добавить ответ",
                                     command=self._add_answer_btn_click)
        self.add_answer_btn.grid(row=2, column=0)

        self.remove_answer_btn = Button(self.add_checkButtonQuestion_window, text="Удалить ответ",
                                        command=self._remove_answer_btn_click)
        self.remove_answer_btn.grid(row=2, column=1)

        self.add_question_btn = Button(self.add_checkButtonQuestion_window, text="Добавить вопрос",
                                       command=self._add_question_btn_click)
        self.add_question_btn.grid(row=3, column=0)

        self.save_changes_btn = Button(self.add_checkButtonQuestion_window, text="Сохранить изменения",
                                       command=self._save_changes_btn_click)
        self.save_changes_btn.grid(row=4, column=0)

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
            selected_id = IntVar(self.add_checkButtonQuestion_window)
            selected_id.set(len(self.answers) + 1)
            self.selections.append(selected_id)

            answer_btn = Checkbutton(self.add_checkButtonQuestion_window, text=self.answers[i].text,
                                     offvalue=len(self.answers) + 1,
                                     onvalue=i,
                                     variable=selected_id)

            if self.answers[i].is_correct:
                answer_btn["fg"] = "green"

            answer_btn.grid(row=i+2, column=2)
            self.check_buttons.append(answer_btn)

    def _clear_checkbuttons(self):
        """Удаляет все инициализированные checkbuttons, ничего не возвращает."""
        for btn in self.check_buttons:
            btn.destroy()
        self.check_buttons.clear()
        self.selections.clear()

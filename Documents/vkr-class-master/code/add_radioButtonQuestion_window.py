from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from typing import List
from questionsStrorage import QuestionsStorage
from validation import Validation
from fileProvider import FileProvider
from question import Question
from answer import Answer
from question_radioButton import QuestionRadioButton


class AddRadioButtonQuestion:
    """Класс AddRadioButtonQuestion - инициализирует окно для добавления вопроса с единственным выбором."""
    new_question: Question

    def __init__(self, questions_storage: QuestionsStorage):
        """Устанавливает все необходимые атрибуты для объекта AddRadioButtonQuestion."""
        self.answers: List[Answer] = []
        self.questions_storage = questions_storage
        self.add_radioButtonQuestion_window = Tk()
        self.add_radioButtonQuestion_window.title('Добавление вопроса с выбором')
        self.add_radioButtonQuestion_window.geometry('900x200')
        self.add_radioButtonQuestion_window.resizable(False, True)
        self.selected_id = IntVar(self.add_radioButtonQuestion_window)
        self.radio_buttons = []

        self.selected_true = BooleanVar(self.add_radioButtonQuestion_window)
        self.selected_true.set(False)

        Label(self.add_radioButtonQuestion_window, text="Текст вопроса:", justify=LEFT).grid(row=0, column=0, sticky=W)
        self.questionText_entry = Entry(self.add_radioButtonQuestion_window, width=30)
        self.questionText_entry.grid(row=0, column=1, sticky=EW)

        Label(self.add_radioButtonQuestion_window, text="Ответ на вопрос:",
              justify=LEFT).grid(row=1, column=0, sticky=W)
        self.answer_entry = Entry(self.add_radioButtonQuestion_window, width=30)
        self.answer_entry.grid(row=1, column=1, sticky=EW)

        self.answer_is_correct_checkBtn = Checkbutton(self.add_radioButtonQuestion_window,
                                                      text="Ответ верный",
                                                      variable=self.selected_true)
        self.answer_is_correct_checkBtn.grid(row=1, column=2)

        self.add_answer_btn = Button(self.add_radioButtonQuestion_window, text="Добавить ответ",
                                     command=self._add_answer_btn_click)
        self.add_answer_btn.grid(row=2, column=0)

        self.remove_answer_btn = Button(self.add_radioButtonQuestion_window, text="Удалить ответ",
                                        command=self._remove_answer_btn_click)
        self.remove_answer_btn.grid(row=2, column=1)

        self.add_question_btn = Button(self.add_radioButtonQuestion_window, text="Добавить вопрос",
                                       command=self._add_question_btn_click)
        self.add_question_btn.grid(row=3, column=0)

        self.save_changes_btn = Button(self.add_radioButtonQuestion_window, text="Сохранить изменения",
                                       command=self._save_changes_btn_click)
        self.save_changes_btn.grid(row=3, column=1)

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

        if self._had_correct_answer() and correctness:
            messagebox.showwarning(title="Предупреждение",
                                   message="В данном типе вопроса может быть только один правильный ответ")
            return

        answer = Answer(input_answer, correctness)
        self.answers.append(answer)
        self._init_radiobuttons()

    def _remove_answer_btn_click(self):
        """Обработчик нажатия кнопки remove_answer_btn - удаляет выбранный пользователем ответ, ничего не возвращает."""
        if len(self.answers) > 0:
            del self.answers[self.selected_id.get()]
            self._init_radiobuttons()

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

        if not self._had_correct_answer():
            messagebox.showwarning(title="Предупреждение",
                                   message="Хотя бы один вопрос должен быть правильным!")
            return

        self.new_question = QuestionRadioButton(question_text, self.answers)
        self.questions_storage.add_question(self.new_question)
        messagebox.showinfo(title="Успешно", message="Вопрос добавлен.")

    def _save_changes_btn_click(self):
        """Обработчик нажатия кнопки save_changes_btn - сохраняет текущие вопросы, ничего не возвращает."""
        FileProvider.save_test_changes(self.questions_storage.test, self.questions_storage.test_path)
        messagebox.showinfo(title="Успешно", message="Изменения сохранены.")

    def _init_radiobuttons(self):
        """Инициализирует radiobuttons в соответствии с вопросами, ничего не возвращает."""
        self._clear_radiobuttons()
        for i in range(len(self.answers)):
            answer_btn = Radiobutton(self.add_radioButtonQuestion_window, text=self.answers[i].text, value=i,
                                     variable=self.selected_id)

            if self.answers[i].is_correct:
                answer_btn["fg"] = "green"

            answer_btn.grid(row=i+2, column=2)
            self.radio_buttons.append(answer_btn)

    def _clear_radiobuttons(self):
        """Удаляет все инициализированные radiobuttons, ничего не возвращает."""
        for btn in self.radio_buttons:
            btn.destroy()
        self.radio_buttons.clear()

    def _had_correct_answer(self):
        """Проверяет наличие правильного ответа, возвращает True - при наличии, False - при отсутствии."""
        one_is_correct = False
        for answer in self.answers:
            if answer.is_correct:
                one_is_correct = True
                break

        return one_is_correct

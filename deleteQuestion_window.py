from tkinter import *
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
from questionsStrorage import QuestionsStorage
from fileProvider import FileProvider


font_header = ('Arial', 15)
font_entry = ('Arial', 12)
lable_font = ('Arial', 11)
base_padding = {'padx': 10, 'pady': 8}
header_padding = {'padx': 10, 'pady': 12}


class DeleteQuestionWindow:
    def __init__(self, questions_storage: QuestionsStorage):
        self.questions_storage = questions_storage
        self.deleteQuestion_window = Tk()
        self.deleteQuestion_window.title('Удаление вопроса')
        self.deleteQuestion_window.geometry('600x700')
        self.deleteQuestion_window.resizable(True, True)

        self.questions_editor = ScrolledText(self.deleteQuestion_window, wrap="word")
        self.questions_editor.pack(fill=BOTH, expand=1)

        self.print_questions()

        self.questionNumber_entry = Entry(self.deleteQuestion_window, bg='#fff', fg='#444', font=font_entry)
        self.questionNumber_entry.pack()

        self.delete_question_btn = Button(self.deleteQuestion_window,
                                          text='Удалить вопрос', command=self.delete_question_btn_click)
        self.delete_question_btn.pack()

        self.save_changes_btn = Button(self.deleteQuestion_window,
                                       text='Сохранить изменения', command=self.save_changes_btn_click)
        self.save_changes_btn.pack()

    def delete_question_btn_click(self):
        question_number = self.questionNumber_entry.get()
        if not question_number.isdigit():
            messagebox.showwarning(title="Предупреждение", message="Введите номер вопроса, целое число.")
            return
        number = int(question_number)

        if number < 1 or number >= self.count:
            messagebox.showwarning(title="Предупреждение",
                                   message="Номер вопроса выходит за границу количества вопросов.")
            return

        self.questions_storage.remove_question(number)
        self.print_questions()
        messagebox.showinfo(title="Уведомление", message="Вопрос успешно удалён. Сохраните изменения.")

    def save_changes_btn_click(self):
        FileProvider.save_test(self.questions)
        messagebox.showinfo(title="Уведомление", message="Изменения сохранены.")

    def print_questions(self):
        self.questions_editor.delete('1.0', END)
        self.questions = self.questions_storage.questions
        self.count = 1
        for q in self.questions:
            self.questions_editor.insert(END, "№{i} {question}\n".format(i=self.count, question=q.text))
            self.count += 1
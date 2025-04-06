from tkinter import *
from tkinter import ttk
from fileProvider import FileProvider
from user import User
from window import Window
import customtkinter


class ResultsWindow(Window):
    """Класс MenuWindow - инициализирует окно результатов тестов."""
    def __init__(self, user: User):
        """Устанавливает все необходимые атрибуты для объекта ResultsWindow."""
        super().__init__()

        self.user = user
        self.title = "Результаты тестов"
        self.width = 600
        self.height = 400
        self.resizable(True, True)

        self._place()

        test_results = FileProvider.get_results()

        self.tuple_results = []
        for result in test_results:
            self.tuple_results.append(
                (
                    result.name,
                    result.right_answers_count,
                    result.right_answers_percentage,
                    result.completion_time
                )
            )

        self.columns = ("name", "rightAnswersCount", "right_answers_percentage", "completion_time")

        self.results_tree = ttk.Treeview(self, columns=self.columns, show="headings")
        self.results_tree.pack(expand=True, fill=BOTH)


        self.results_tree.heading("name", text="Имя", anchor=W)
        self.results_tree.heading("rightAnswersCount", text="Кол-во правильных ответов", anchor=W)
        self.results_tree.heading("right_answers_percentage", text="Процент правильных ответов", anchor=W)
        self.results_tree.heading("completion_time", text="Время завершения", anchor=W)

        self.results_tree.column("#1", stretch=YES, width=120)
        self.results_tree.column("#2", stretch=YES, width=170)
        self.results_tree.column("#3", stretch=YES, width=100)
        self.results_tree.column("#4", stretch=YES, width=140)

        for tuple_result in self.tuple_results:
            self.results_tree.insert("", END, values=tuple_result)

        self.scrollbar = ttk.Scrollbar(self, orient=VERTICAL, command=self.results_tree.yview)
        self.results_tree.configure(yscrollcommand=self.scrollbar.set)
        self.results_tree.pack()

        self.mainloop()

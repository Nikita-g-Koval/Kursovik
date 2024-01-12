from tkinter import *
from tkinter import ttk
from fileProvider import FileProvider


class ResultsWindow:
    def __init__(self):
        self.results_window = Tk()
        self.results_window.title = "Результаты тестов"
        self.results_window.geometry("510x200")
        self.results_window.resizable(True, True)

        test_results = FileProvider.get_results()

        self.tuple_results = []
        for result in test_results:
            self.tuple_results.append(
                (
                    result.user.name,
                    result.right_answers_count,
                    result.diagnose.grade,
                    result.completion_time
                )
            )

        self.columns = ("name", "rightAnswersCount", "diagnose", "completion_time")

        self.results_tree = ttk.Treeview(self.results_window, columns=self.columns, show="headings")
        self.results_tree.pack(expand=True, fill=BOTH)

        self.results_tree.heading("name", text="Имя", anchor=W)
        self.results_tree.heading("rightAnswersCount", text="Кол-во правильных ответов", anchor=W)
        self.results_tree.heading("diagnose", text="Диагноз", anchor=W)
        self.results_tree.heading("completion_time", text="Время завершения", anchor=W)

        self.results_tree.column("#1", stretch=NO, width=120)
        self.results_tree.column("#2", stretch=NO, width=170)
        self.results_tree.column("#3", stretch=NO, width=100)
        self.results_tree.column("#4", stretch=NO, width=140)

        for tuple_result in self.tuple_results:
            self.results_tree.insert("", END, values=tuple_result)

        self.scrollbar = ttk.Scrollbar(self.results_window, orient=VERTICAL, command=self.results_tree.yview)
        self.results_tree.configure(yscrollcommand=self.scrollbar.set)
        self.results_tree.pack()

from tkinter import *
from tkinter import ttk

from matplotlib import pyplot as plt

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
        self.title("Результаты тестов")
        self.width = 600
        self.height = 400
        self.resizable(True, True)

        self._place()

        self.test_results = FileProvider.get_results()

        self.tuple_results = []

        if self.user.name == "Администратор":

            self.diagram_button = customtkinter.CTkButton(self, text="Диаграмма", command=self.diagram_button_click)
            self.diagram_button.pack()

            for result in self.test_results:
                self.tuple_results.append(
                    (
                        result.user_name,
                        result.test_name,
                        result.right_answers_count,
                        result.right_answers_percentage,
                        result.completion_time
                    )
                )
        else:
            for result in self.test_results:
                if result.user_name == user.name:
                    self.tuple_results.append(
                        (
                            result.user_name,
                            result.test_name,
                            result.right_answers_count,
                            result.right_answers_percentage,
                            result.completion_time
                        )
                    )


        self.columns = ("user_name", "test_name", "rightAnswersCount", "right_answers_percentage", "completion_time")

        self.results_tree = ttk.Treeview(self, columns=self.columns, show="headings")
        self.results_tree.pack(expand=True, fill=BOTH, padx=10, pady=10)


        self.results_tree.heading("user_name", text="Пользователь", anchor=W)
        self.results_tree.heading("test_name", text="Тест", anchor=W)
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
        self.results_tree.bind("<Double-1>", self.OnDoubleClick)
        self.results_tree.pack()

        self.protocol("WM_DELETE_WINDOW", self.destroy)

        self.mainloop()

    def diagram_button_click(self):
        vals = []
        labels = []

        for result in self.test_results:
            user_name = result.user_name
            if user_name not in labels:
                labels.append(user_name)
                best_result = self.find_best_result_for(user_name)
                vals.append(best_result)

        plt.bar(labels, vals, label='Лучший результат')

        for i in range(len(vals)):
            plt.text(i, vals[i], vals[i], ha='center')  # Aligning text at center

        plt.xlabel('Имя')
        plt.ylabel('Процент правильных ответов')
        plt.title('Столбчатая диаграмма прошедших тесты')
        plt.legend()
        plt.show()

    def find_best_result_for(self, user_name: str):
        best_result = 0

        for result in self.test_results:
            if result.user_name != user_name:
                continue

            if result.right_answers_percentage >= best_result:
                best_result = result.right_answers_percentage

        return best_result

    def OnDoubleClick(self, event):
        item = self.results_tree.selection()[0]
        print("you clicked on", self.results_tree.item(item, "values"))

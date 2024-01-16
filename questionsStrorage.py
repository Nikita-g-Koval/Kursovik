from fileProvider import FileProvider
from test import Test


class QuestionsStorage:
    """Класс QuestionsStorage, описывающий хранилище вопросов."""

    def __init__(self, test_path: str):
        """Устанавливает все необходимые атрибуты для объекта QuestionsStorage."""
        self.test: Test = FileProvider.get_test(test_path)
        self.test_path = test_path

    def add_question(self, question):
        """Добавляет вопрос в хранилище."""
        self.test.questions.append(question)

    def remove_question(self, question_number):
        """Удаляет вопрос по индексу из хранилища."""
        del self.test.questions[question_number - 1]

    def update_test(self, test_path: str):
        """Обновляет тест по указанному пути и сохраняет путь, по которому был обновлён тест."""
        self.test = FileProvider.get_test(test_path)
        self.test_path = test_path

    def save_changes(self):
        """Сохраняет изменения по пути текущего теста."""
        FileProvider.save_test_changes(self.test, self.test_path)

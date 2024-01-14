import os
from random import randint
from question import Question
from question_radioButton import QuestionRadioButton
from question_checkButton import QuestionCheckButton
from answer import Answer
from fileProvider import FileProvider


class QuestionsStorage:
    """Класс QuestionsStorage, описывающий хранилище вопросов."""
    questions = []

    def __init__(self):
        """Устанавливает все необходимые атрибуты для объекта QuestionsStorage."""
        self.test_path: str = "Tests\\base_questions.json"

        self.questions = FileProvider.get_questions(self.test_path)

    @property
    def test_name(self):
        """Getter свойства test_name, возвращает название теста."""
        return os.path.basename(self.test_path).split('.')[0]

    def add_question(self, question):
        """Добавляет вопрос в хранилище."""
        self.questions.append(question)

    def remove_question(self, question_number):
        """Удаляет вопрос по индексу из хранилища."""
        del self.questions[question_number - 1]

    @staticmethod
    def shuffle(mas: []):
        """Перемешивает переданный список и возвращает его."""
        result = mas
        list_length = len(result)
        for i in range(list_length):
            index_aleatory = randint(0, list_length - 1)
            temp = result[i]
            result[i] = result[index_aleatory]
            result[index_aleatory] = temp
        return result

    def update_questions(self, test_path: str):
        """Обновляет вопросы хранилища по указанному пути и сохраняет путь, по которому были обновлены вопросы."""
        self.questions.clear()
        self.questions = FileProvider.get_questions(test_path)
        self.test_path = test_path

    def save_questions(self):
        """Сохраняет вопросы по пути текущего теста."""
        FileProvider.save_test(self.questions, self.test_name())

import os
from random import randint
from question import Question
from question_radioButton import QuestionRadioButton
from question_checkButton import QuestionCheckButton
from answer import Answer
from fileProvider import FileProvider


class QuestionsStorage:
    """Класс QuestionsStorage описывающий хранилище вопросов."""
    questions = []

    base_questions = [
        Question("Сколько будет два плюс два умноженное на два?",
                 [Answer('6', True)]),
        QuestionRadioButton("Бревно нужно распилить на 10 частей. Сколько распилов нужно сделать?",
                            [Answer('5', False), Answer('9', True), Answer('10', False), Answer('11', False)]),
        QuestionCheckButton("На двух руках 10 пальцев. Сколько пальцев на 5 руках?",
                            [Answer('10', False), Answer('25', True), Answer('50', False), Answer('15', False)]),
    ]

    def __init__(self):
        """Устанавливает все необходимые атрибуты для объекта QuestionsStorage."""
        self.test_path: str = "Tests\\BaseQuestions.json"

        self.questions = self.base_questions

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

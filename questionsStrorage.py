from random import randint
from question import Question


class QuestionsStorage:
    def __init__(self):
        self.questions = [
            Question("Сколько будет два плюс два умноженное на два?", 6),
            Question("Бревно нужно распилить на 10 частей. Сколько распилов нужно сделать?", 9),
            Question("На двух руках 10 пальцев. Сколько пальцев на 5 руках?", 25),
            Question("Укол делают каждые полчаса. Сколько нужно минут, чтобы сделать три укола?", 60),
            Question("Пять свечей горело, две потухли. Сколько свечей осталось?", 5)
        ]

    def add_question(self, question):
        self.questions.append(question)

    def remove_question(self, id):
        del self.questions[id - 1]

    def shuffle(self):
        result = self.questions
        list_length = len(result)
        for i in range(list_length):
            index_aleatory = randint(0, list_length - 1)
            temp = result[i]
            result[i] = result[index_aleatory]
            result[index_aleatory] = temp
        return result

from random import random


class QuestionStorage:
    questions = []
    questionsCount = questions.count()

    def __init__(self, questions):
        self.questions = questions

    def AddQuestion(self, question):
        self.questions.Append(question)

    def RemoveQuestion(self, id):
        del self.questions[id - 1]

    def Shuffle(self, questions):
        result = questions[:]
        list_length = len(result)
        for i in range(list_length):
            index_aleatory = random.randint(0, list_length - 1)
            temp = result[i]
            result[i] = result[index_aleatory]
            result[index_aleatory] = temp
        # Возвращаем список
        return result

import os
import json
from typing import List
from random import randint
from question import Question
from answer import Answer
from fileProvider import FileProvider


class QuestionsStorage:
    questions = []

    def __init__(self):
        if os.path.exists(FileProvider.questionsFileName):
            self.update_questions()
            return

        self.questions = [
            Question("Сколько будет два плюс два умноженное на два?",
                     [Answer('8', False), Answer('6', True), Answer('12', False)]),
            Question("Бревно нужно распилить на 10 частей. Сколько распилов нужно сделать?",
                     [Answer('5', False), Answer('9', True), Answer('10', False), Answer('11', False)]),
            Question("На двух руках 10 пальцев. Сколько пальцев на 5 руках?",
                     [Answer('10', False), Answer('25', True), Answer('50', False), Answer('15', False)]),
            Question("Укол делают каждые полчаса. Сколько нужно минут, чтобы сделать три укола?",
                     [Answer('5', False), Answer('9', True), Answer('10', False), Answer('11', False)]),
            Question("Пять свечей горело, две потухли. Сколько свечей осталось?",
                     [Answer('2', False), Answer('5', True), Answer('0', False), Answer('3', False)])
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

    def update_questions(self):
        if not os.path.exists(FileProvider.questionsFileName):
            return

        self.questions.clear()
        questions = FileProvider.get_questions()

        for q in questions:
            answers = []
            for answer in q['answers']:
                answers.append(Answer(answer['text'], answer['is_correct']))
            self.questions.append(Question(q['text'], answers))




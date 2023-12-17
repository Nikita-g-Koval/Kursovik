import os
import json
from typing import List
from random import randint
from question import Question
from question_radioButton import QuestionRadioButton
from question_checkButton import QuestionCheckButton
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
                     [Answer('6', True)]),
            QuestionRadioButton("Бревно нужно распилить на 10 частей. Сколько распилов нужно сделать?",
                                [Answer('5', False), Answer('9', True), Answer('10', False), Answer('11', False)]),
            QuestionCheckButton("На двух руках 10 пальцев. Сколько пальцев на 5 руках?",
                                [Answer('10', False), Answer('25', True), Answer('50', False), Answer('15', False)]),
        ]

    def add_question(self, question):
        self.questions.append(question)

    def remove_question(self, id):
        del self.questions[id - 1]

    @staticmethod
    def shuffle(mas: []):
        result = mas
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




from answer import Answer
from question_type import QuestionType
from typing import List


class Question:
    _answers: List[Answer]

    def __init__(self, text: str, answers: List[Answer]):
        self.text = text
        self.answers = answers

    @property
    def answers(self):
        return self._answers

    @answers.setter
    def answers(self, answers: List[Answer]):
        self._answers = answers

    @property
    def get_type(self):
        return QuestionType.base

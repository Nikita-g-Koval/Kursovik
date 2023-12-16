from answer import Answer
from question_type import QuestionType


class Question:
    def __init__(self, text: str, answer: Answer):
        self.text = text
        self.answer = answer

    def get_type(self):
        return QuestionType.base

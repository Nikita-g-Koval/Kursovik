from answer import Answer
from typing import List


class Question:
    def __init__(self, text: str, answers: List[Answer]):
        self.text = text
        self.answers = answers

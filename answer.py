import json


class Answer:
    def __init__(self, text: str, is_correct: bool):
        self.text = text
        self.is_correct = is_correct

from answer import Answer


class Question:
    def __init__(self, text: str, answer: Answer):
        self.text = text
        self.answer = answer

class Answer:
    """Класс Answer для представления ответа вопроса."""
    def __init__(self, text: str, is_correct: bool = False):
        self.text = text
        self.is_correct = is_correct

    def __eq__(self, other):
        if self.text == other.text and self.is_correct == other.is_correct:
            return True

        return False

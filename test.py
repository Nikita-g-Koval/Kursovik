from typing import List
from question import Question


class Test:
    """Класс Test для описания теста."""
    def __init__(self, name: str, questions: List[Question]):
        """Устанавливает все необходимые атрибуты для объекта Test."""
        self.name = name
        self.questions = questions

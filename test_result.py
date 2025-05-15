from user import User
from datetime import datetime


class TestResult:
    """Класс TestResult описывает результат теста."""
    name: str
    right_answers_count: int
    right_answers_percentage: float
    completion_time: datetime

    def __init__(self, name, right_answers_count: int, right_answers_percentage: float, completion_time: datetime):
        """Устанавливает все необходимые атрибуты для объекта TestResult."""
        self.name = name
        self.right_answers_count = right_answers_count
        self.right_answers_percentage = right_answers_percentage
        self.completion_time = completion_time

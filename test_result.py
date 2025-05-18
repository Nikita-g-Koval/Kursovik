from user import User
from datetime import datetime


class TestResult:
    """Класс TestResult описывает результат теста."""
    user_name: str
    test_name: str
    right_answers_count: int
    right_answers_percentage: float
    completion_time: datetime

    def __init__(self, user_name, test_name, right_answers_count: int, right_answers_percentage: float, completion_time: datetime):
        """Устанавливает все необходимые атрибуты для объекта TestResult."""
        self.user_name = user_name
        self.test_name = test_name
        self.right_answers_count = right_answers_count
        self.right_answers_percentage = right_answers_percentage
        self.completion_time = completion_time

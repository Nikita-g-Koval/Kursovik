from user import User
from diagnosis import Diagnosis
from datetime import datetime


class TestResult:
    """Класс TestResult описывает результат теста."""
    user: User
    right_answers_count: int
    diagnose: Diagnosis
    completion_time: datetime

    def __init__(self, user: User, right_answers_count: int, diagnose: Diagnosis, completion_time: datetime):
        """Устанавливает все необходимые атрибуты для объекта TestResult."""
        self.user = user
        self.right_answers_count = right_answers_count
        self.diagnose = diagnose
        self.completion_time = completion_time

from user import User
from datetime import datetime
from diagnosis import Diagnosis
from datetime import datetime


class TestResult:
    user: User
    right_answers_count: int
    diagnose: Diagnosis
    completion_time: datetime

    def __init__(self, user: User, right_answers_count: int, diagnose: Diagnosis, completion_time: datetime):
        self.user = user
        self.right_answers_count = right_answers_count
        self.diagnose = diagnose
        self.completion_time = completion_time

from typing import List
from answer import Answer
from question import Question
from question_type import QuestionType
from random import randint
from diagnosis import Diagnosis
from diagnosesStorage import DiagnosesStorage
from test_result import TestResult


class Test:
    """Класс Test для описания теста."""
    _current_question_id: int = None
    _current_answers: List[Answer] = None

    def __init__(self, name: str, questions: List[Question]):
        """Устанавливает все необходимые атрибуты для объекта Test."""
        self.name = name
        self.questions = questions

        self.diagnosesStorage = DiagnosesStorage()

        self.score = 0
        self.is_started = False

    @property
    def get_current_question(self):
        """Возвращает текущий вопрос."""
        if not self.is_started:
            raise Exception("Тест не был запущен! Сначала запустите его.")

        return self.questions[self._current_question_id]

    def print_current_question(self):
        """Возвращает номер вопроса и его текст."""
        if not self.is_started:
            raise Exception("Тест не был запущен! Сначала запустите его.")

        return f"№{self._current_question_id + 1}. {self.get_current_question.text}"

    @property
    def get_current_answers(self):
        """Возвращает ответы текущего вопроса."""
        if not self.is_started:
            raise Exception("Тест не был запущен! Сначала запустите его.")

        self._current_answers = self.get_current_question.answers
        return self._current_answers

    @property
    def is_finished(self):
        """Возвращает статус завершения теста."""
        if self._current_question_id >= len(self.questions):
            return True

        return False

    @staticmethod
    def shuffle(mas: []):
        """Перемешивает переданный список и возвращает его."""
        result = mas
        list_length = len(result)
        for i in range(list_length):
            index_aleatory = randint(0, list_length - 1)
            temp = result[i]
            result[i] = result[index_aleatory]
            result[index_aleatory] = temp
        return result

    def shuffle_questions(self):
        """Перемешивает вопросы текущего теста, ничего не возвращает."""
        self.questions = self.shuffle(self.questions)

    def shuffle_answers(self):
        """Перемешивает ответы текущего вопроса, ничего не возвращает."""
        self.shuffle(self.get_current_answers)

    def start_test(self):
        """Запускает тест, обнуляет счёт и устанавливает id текущего вопроса, ничего не возвращает."""
        self.is_started = True
        self._current_question_id = 0
        self.score = 0
        self.shuffle_questions()
        self.shuffle_answers()

    def next_question(self):
        """Делает инкремент id текущего вопроса и перемешивает его ответы, ничего не возвращает."""
        self._current_question_id += 1

        if self.is_finished:
            return

        self.shuffle_answers()

    def accept_answer_base(self, answer: str):
        """Проверяет ответ на базовый вопрос и увеличивает счёт, если ответ правильный. Ничего не возвращает."""
        if self.get_current_question.get_type != QuestionType.base:
            raise Exception(f"Текущий вопрос имеет тип {self.get_current_question.get_type}, а не {QuestionType.base}")

        if answer == self.get_current_answers[0].text:
            self.score += 1

    def accept_answer_radio(self, answer: Answer):
        """Проверяет ответ на вопрос с единственным выбором и увеличивает счёт, если ответ правильный."""
        if self.get_current_question.get_type != QuestionType.radio_button:
            raise Exception(
                f"Текущий вопрос имеет тип {self.get_current_question.get_type}, а не {QuestionType.radio_button}")

        if answer.is_correct:
            self.score += 1

    def accept_answer_check(self, answers: List[Answer]):
        """Проверяет ответ на вопрос с множественным выбором и увеличивает счёт, если ответы правильные."""
        if self.get_current_question.get_type != QuestionType.check_button:
            raise Exception(
                f"Текущий вопрос имеет тип {self.get_current_question.get_type}, а не {QuestionType.check_button}")

        attempts = 0
        successful_attempts = 0

        for answer in answers:
            attempts += 1
            if answer.is_correct:
                successful_attempts += 1

        if attempts == 0:
            successful_percentage = 0
        else:
            successful_percentage = successful_attempts / attempts * 100

        if successful_percentage > 50:
            self.score += 1

    def summarise(self):
        """Возвращает диагноз соответствующий результату теста."""
        if not self.is_finished:
            raise Exception("Чтобы подвести итог, пройдите тест до конца.")

        diagnosis = self.diagnosesStorage.calculate_diagnose(len(self.questions), self.score)

        return diagnosis

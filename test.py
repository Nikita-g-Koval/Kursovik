from typing import List
from answer import Answer
from question import Question
from question_type import QuestionType
from random import randint
from test_result import TestResult


class Test:
    """Класс Test для описания теста."""
    _current_question_id: int = None
    _current_answers: List[Answer] = None

    def __init__(self, name: str, questions: List[Question]):
        """Устанавливает все необходимые атрибуты для объекта Test."""
        self.name = name
        self.questions = questions
        self.score = 0
        self.is_started = False

    @property
    def questions_count(self):
        """Возвращает количество вопросов."""
        return len(self.questions)

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
        if self._current_question_id >= self.questions_count:
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

    def accept_answers(self, user_answers: List[Answer]):
        """Проверяет ответ на базовый вопрос и увеличивает счёт, если ответ правильный. Ничего не возвращает."""
        if self.get_current_question.varify_answers(user_answers):
            self._increase_score()

    def _increase_score(self):
        """Увеличивает счёт, ничего не возвращает."""
        self.score += 1

    @staticmethod
    def calculate_right_answers_percentage(questions_count, right_answers_count):
        """Расчитывает отношение правильных ответов к количеству вопросов, возвращает процентное соотношение."""
        right_answers_percentage = right_answers_count * 100 / questions_count

        return right_answers_percentage

    def summarise(self):
        """Возвращает диагноз соответствующий результату теста."""
        if not self.is_finished:
            raise Exception("Чтобы подвести итог, пройдите тест до конца.")

        right_answers_percentage = self.calculate_right_answers_percentage(len(self.questions), self.score)

        return right_answers_percentage

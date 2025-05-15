from answer import Answer
from question_type import QuestionType
from typing import List


class Question:
    """Класс Question для описания вопроса."""
    _answers: List[Answer]

    def __init__(self, text: str, answers: List[Answer]):
        """Устанавливает все необходимые атрибуты для объекта Question."""
        self.text = text
        self.answers = answers

    @property
    def answers(self):
        """Getter свойства answers, возвращает список ответов."""
        return self._answers

    @answers.setter
    def answers(self, answers: List[Answer]):
        """Setter свойства answers, устанавливает список ответов."""
        self._answers = answers

    @property
    def get_type(self):
        """Getter свойства get_type, возвращает тип вопроса."""
        return QuestionType.base

    def varify_answers(self, user_answers: List[Answer]):
        """Проверяет переданный ответ, возвращает True или False."""
        for answer in self.answers:
            for user_answer in user_answers:
                if answer.is_correct and answer.text == user_answer.text:
                    return True

        return False


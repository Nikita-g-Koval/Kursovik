from question_radioButton import QuestionRadioButton
from answer import Answer
from typing import List
from question_type import QuestionType


class QuestionCheckButton(QuestionRadioButton):
    """Класс QuestionCheckButton, описывающий вопрос с множественным выбором. Наследник класса QuestionRadioButton."""
    @property
    def get_type(self):
        return QuestionType.check_button

    @QuestionRadioButton.answers.setter
    def answers(self, answers: List[Answer]):
        """Setter свойства answers, устанавливает список ответов."""
        self._answers = answers

    def varify_answers(self, user_answers: List[Answer]):
        """Проверяет список ответов, возвращает True, если большая часть ответов правильна или False."""
        attempts = len(user_answers)
        successful_attempts = 0

        if attempts == 0:
            return False

        for answer in self.answers:
            for user_answer in user_answers:
                if answer == user_answer and answer.is_correct:
                    successful_attempts += 1

        successful_percentage = successful_attempts / attempts * 100

        if successful_percentage > 50:
            return True

        return False

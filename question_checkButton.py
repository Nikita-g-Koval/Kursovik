from question_radioButton import QuestionRadioButton
from answer import Answer
from typing import List
from question_type import QuestionType


class QuestionCheckButton(QuestionRadioButton):
    """Класс QuestionCheckButton описывающий вопрос с множественным выбором. Наследник класса QuestionRadioButton."""
    @property
    def get_type(self):
        return QuestionType.check_button

    @QuestionRadioButton.answers.setter
    def answers(self, answers: List[Answer]):
        """Setter свойства answers, устанавливает список ответов."""
        self._answers = answers

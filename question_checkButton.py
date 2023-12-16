from question_radioButton import QuestionRadioButton
from answer import Answer
from typing import List
from question_type import QuestionType


class QuestionCheckButton(QuestionRadioButton):
    def get_type(self):
        return QuestionType.check_button
    @QuestionRadioButton.answers.setter
    def answers(self, answers: List[Answer]):
        self._answers = answers

from question_radioButton import QuestionRadioButton
from answer import Answer
from typing import List


class QuestionCheckButton(QuestionRadioButton):
    @QuestionRadioButton.answers.setter
    def answers(self, answers: List[Answer]):
        self._answers = answers

from question import Question
from answer import Answer
from typing import List


class QuestionRadioButton(Question):
    _answers: List[Answer]

    def __init__(self, text: str, answers: List[Answer]):
        Question.__init__(text, None)
        self.text = text
        self.answers = answers

    @property
    def answers(self):
        return self._answers

    @answers.setter
    def answers(self, answers: List[Answer]):
        for answer in answers:
            count_of_correct_ones = 0
            if answer.is_correct:
                count_of_correct_ones += 1
            if count_of_correct_ones > 1:
                raise Exception('В классе QuestionRadioButton возможен только один правильный ответ.')

        self._answers = answers

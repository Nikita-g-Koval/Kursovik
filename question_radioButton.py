from question import Question
from answer import Answer
from typing import List
from question_type import QuestionType


class QuestionRadioButton(Question):
    """Класс QuestionRadioButton, описывающий вопрос с единственным выбором. Наследник класса Question."""
    def __init__(self, text: str, answers: List[Answer]):
        Question.__init__(self, text, answers)
        self.text = text
        self.answers = answers

    @property
    def get_type(self):
        return QuestionType.radio_button

    @Question.answers.setter
    def answers(self, answers: List[Answer]):
        """Setter свойства answers, устанавливает список ответов."""
        for answer in answers:
            count_of_correct_ones = 0
            if answer.is_correct:
                count_of_correct_ones += 1
            if count_of_correct_ones > 1:
                raise Exception('В классе QuestionRadioButton возможен только один правильный ответ.')

        self._answers = answers

from user import User
from question import Question
from question_radioButton import QuestionRadioButton
from question_checkButton import QuestionCheckButton
from question_type import QuestionType
from answer import Answer
import os
import json


class FileProvider:
    resultsFileName = "testResults.json"
    questionsFileName = "questions.json"

    @staticmethod
    def save_test_result(user: User):
        json_data = {'users': []}

        if os.path.exists(FileProvider.resultsFileName):
            json_data = FileProvider.get_results()

        json_data['users'].append({
            'name': user.name,
            'rightAnswersCount': user.rightAnswersCount
        })

        with open(FileProvider.resultsFileName, 'w') as outfile:
            json.dump(json_data, outfile, indent=4)

    @staticmethod
    def get_results():
        if not os.path.exists(FileProvider.resultsFileName):
            with open(FileProvider.resultsFileName) as json_file:
                json_data = json.load(json_file)
            return json_data

    @staticmethod
    def clear_test_results():
        if os.path.exists(FileProvider.resultsFileName):
            os.remove(FileProvider.resultsFileName)

    @staticmethod
    def save_questions(questions):
        data = {
            'questions': []
        }

        for question in questions:
            answers = []
            for answer in question.answers:
                answers.append({
                    'text': answer.text,
                    'is_correct': answer.is_correct
                })

            data['questions'].append({
                'type': int(question.get_type),
                'text': question.text,
                'answers': answers
            })

        with open(FileProvider.questionsFileName, 'w') as outfile:
            json.dump(data, outfile, indent=4)

    @staticmethod
    def get_questions():
        if not os.path.exists(FileProvider.questionsFileName):
            return

        with open(FileProvider.questionsFileName, 'r', encoding='utf-8') as f:
            json_data = json.load(f)

        questions = []

        for question in json_data['questions']:
            answers = []
            for answer in question['answers']:
                answers.append(Answer(
                    text=answer['text'],
                    is_correct=answer['is_correct']
                ))

            question_type: QuestionType = question['type']

            match question_type:
                case QuestionType.base:
                    current_question = Question(
                        text=question['text'],
                        answers=answers
                    )
                case QuestionType.radio_button:
                    current_question = QuestionRadioButton(
                        text=question['text'],
                        answers=answers
                    )
                case QuestionType.check_button:
                    current_question = QuestionCheckButton(
                        text=question['text'],
                        answers=answers
                    )

            questions.append(current_question)

        return questions


def class_to_dict(obj):
    return obj.__dict__

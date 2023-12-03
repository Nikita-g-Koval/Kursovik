from user import User
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
        json_data = json.dumps(questions, default=class_to_dict, indent=4)

        # for question in questions:
        #     json_answers = json.dumps(question.answers, default=class_to_dict)
        #
        #     json_data['questions'].append({
        #         'question_text': question.text,
        #         'answers': json_answers
        #     })

        with open(FileProvider.questionsFileName, 'w') as outfile:
            json.dump(questions, outfile, indent=4, default=class_to_dict)

    @staticmethod
    def get_questions():
        if not os.path.exists(FileProvider.questionsFileName):
            return

        with open(FileProvider.questionsFileName, 'r', encoding='utf-8') as f:
            json_data = json.load(f)

        return json_data


def class_to_dict(obj):
    return obj.__dict__

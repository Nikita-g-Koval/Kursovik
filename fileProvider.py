from user import User
from question import Question
from test import Test
from question_radioButton import QuestionRadioButton
from question_checkButton import QuestionCheckButton
from question_type import QuestionType
from answer import Answer
from diagnosis import Diagnosis
from test_result import TestResult
from datetime import datetime
from typing import List
import os
from os import walk
import json


class FileProvider:
    """Класс FileProvider служит для работы с файловой системой."""
    usersFileName = "users.json"
    resultsFileName = "testResults.json"
    questionsFileName = "questions.json"
    tests_path = os.path.abspath("Tests")

    @staticmethod
    def save_user(user: User):
        json_data = {'users': []}

        if os.path.exists(FileProvider.usersFileName):
            users = FileProvider.get_users()
            for old_user in users:
                json_data['users'].append({
                    'name': old_user.name,
                    'password': old_user.password
                })

        json_data['users'].append({
            'name': user.name,
            'password': user.password
        })

        with open(FileProvider.usersFileName, 'w') as outfile:
            json.dump(json_data, outfile, indent=4)

    @staticmethod
    def get_users():
        users = []

        if os.path.exists(FileProvider.usersFileName):
            with open(FileProvider.usersFileName) as json_file:
                json_data = json.load(json_file)

            for user in json_data['users']:
                new_user = User(user['name'], user['password'])
                users.append(new_user)

        return users


    @staticmethod
    def save_test_result(test_result: TestResult):
        """Сохраняет переданный результат теста, ничего не возвращает."""
        json_data = {'results': []}

        if os.path.exists(FileProvider.resultsFileName):
            results = FileProvider.get_results()
            for result in results:
                json_data['results'].append({
                    'name': result.user.name,
                    'rightAnswersCount': result.right_answers_count,
                    'diagnose': result.diagnose.grade,
                    'completion_time': result.completion_time.strftime('%Y-%m-%d %H:%M:%S')
                })

        json_data['results'].append({
            'name': test_result.user.name,
            'rightAnswersCount': test_result.right_answers_count,
            'diagnose': test_result.diagnose.grade,
            'completion_time': test_result.completion_time.strftime('%Y-%m-%d %H:%M:%S')
        })

        with open(FileProvider.resultsFileName, 'w') as outfile:
            json.dump(json_data, outfile, indent=4)

    @staticmethod
    def get_results():
        """Получает результаты тестов из файла, возвращает список результатов."""
        if os.path.exists(FileProvider.resultsFileName):
            with open(FileProvider.resultsFileName) as json_file:
                json_data = json.load(json_file)

            test_results = []

            for result in json_data['results']:
                user = User(result['name'])
                test_results.append(TestResult(
                    user=user,
                    right_answers_count=result['rightAnswersCount'],
                    diagnose=Diagnosis(result['diagnose']),
                    completion_time=datetime.strptime(result['completion_time'], '%Y-%m-%d %H:%M:%S')
                ))

        return test_results

    @staticmethod
    def clear_test_results():
        """Удаляет все результаты тестов."""
        if os.path.exists(FileProvider.resultsFileName):
            os.remove(FileProvider.resultsFileName)

    @staticmethod
    def save_test(test: Test):
        """Сохраняет переданные вопросы под переданным именем. Ничего не возвращает."""
        data = {
            'test_name': test.name,
            'questions': []
        }

        for question in test.questions:
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

        path = FileProvider.tests_path + f'\\{test.name}.json'

        with open(path, 'w') as outfile:
            json.dump(data, outfile, indent=4)

    @staticmethod
    def get_test(test_path: str):
        """Получает тест по переданному пути, возвращает полученный тест."""
        if not os.path.exists(test_path):
            return

        with open(test_path, 'r', encoding='utf-8') as f:
            json_data = json.load(f)

        if len(json_data) == 0:
            return []

        test_name = json_data['test_name']
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

        test = Test(test_name, questions)

        return test

    @staticmethod
    def save_test_changes(test: Test, test_path: str):
        """Сохраняет переданные вопросы под переданным именем. Ничего не возвращает."""
        data = {
            'test_name': test.name,
            'questions': []
        }

        for question in test.questions:
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

        with open(test_path, 'w') as outfile:
            json.dump(data, outfile, indent=4)

    @staticmethod
    def get_test_names():
        """Получает все сохранённые тесты, возвращает список названий тестов."""
        test_names: List[str] = []
        for (dirpath, dirnames, filenames) in walk(FileProvider.tests_path):
            for filename in filenames:
                test_path = f"{FileProvider.tests_path}\\{filename}"

                with open(test_path, 'r', encoding='utf-8') as f:
                    json_data = json.load(f)

                test_name = json_data['test_name']
                test_names.append(test_name)
            break

        return test_names

    @staticmethod
    def find_test_path(wanted_test_name: str):
        """Находит путь к тесту по его имени, возвращает путь."""
        for (dirpath, dirnames, filenames) in walk(FileProvider.tests_path):
            for filename in filenames:
                test_path = f"{FileProvider.tests_path}\\{filename}"

                with open(test_path, 'r', encoding='utf-8') as f:
                    json_data = json.load(f)

                test_name = json_data['test_name']

                if test_name == wanted_test_name:
                    return test_path
            break

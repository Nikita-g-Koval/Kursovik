from user import User
import os
import json


class FileProvider:
    resultsFileName = "testResults.json"
    questionsFileName = "questions.json"

    def save_test_result(self, user: User):
        json_data = {'users': []}

        if os.path.exists(self.resultsFileName):
            json_data = self.get_results()

        json_data['users'].append({
            'name': user.name,
            'rightAnswersCount': user.rightAnswersCount
        })

        with open(self.resultsFileName, 'w') as outfile:
            json.dump(json_data, outfile, indent=4)

    def get_results(self):
        if not os.path.exists(self.resultsFileName):
            with open(self.resultsFileName) as json_file:
                json_data = json.load(json_file)
            return json_data

    def clear_test_results(self):
        if os.path.exists(self.resultsFileName):
            os.remove(self.resultsFileName)
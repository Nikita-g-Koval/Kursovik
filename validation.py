from questionsStrorage import QuestionStorage


class Validation:
    def ValidateUserName(self, username):
        if len(username) < 2 and not str.isalpha(username):
            return False
        return True


    def ValidateQuestion(self, question):
        if len(question) == 0 or len(question) > 120 or len(question) < 4:
            return False
        return True

    def ValidateAnswer(self, answer):
        if str.isdigit(answer):
            return True
        return False

    def ValidateQuestionNumber(self, number, questions_storage : QuestionStorage):
        if str.isdigit(number) and int(number) < 1 or int(number) > questions_storage.questionsCount:
            return False
        return  True




class Validation:
    @staticmethod
    def ValidateUserName(username):
        if len(username) < 2 or not str.isalpha(username):
            return False
        return True

    @staticmethod
    def ValidateQuestion(question):
        if len(question) > 120 or len(question) < 4:
            return False
        return True

    @staticmethod
    def ValidateAnswer(answer):
        if len(answer) > 1:
            return True
        return False




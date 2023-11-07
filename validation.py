class Validation:
    def ValidateUserName(username):
        if len(username) < 2 or not str.isalpha(username):
            return False
        return True


    def ValidateQuestion(question):
        if len(question) == 0 or len(question) > 120 or len(question) < 4:
            return False
        return True

    def ValidateAnswer(answer):
        if str.isdigit(answer):
            return True
        return False




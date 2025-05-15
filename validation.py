class Validation:
    """Класс Validation служит для проверки ввода пользователя."""
    @staticmethod
    def validate_user_name(username):
        """Проверяет имя пользователя, возвращает True, если имя подходит условиям, иначе - False."""
        if len(username) < 2 or not str.isalpha(username):
            return False

        return True

    @staticmethod
    def validate_question(question):
        """Проверяет вопрос пользователя, возвращает True, если подходит условиям, иначе - False."""
        if len(question) > 120 or len(question) < 4:
            return False
        return True

    @staticmethod
    def validate_answer(answer):
        """Проверяет ответ пользователя, возвращает True, если подходит условиям, иначе - False."""
        if len(answer) > 1:
            return True
        return False

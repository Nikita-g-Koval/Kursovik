import fileProvider


class Validation:
    """Класс Validation служит для проверки ввода пользователя."""
    @staticmethod
    def validate_user_name(username: str):
        """Проверяет имя пользователя, возвращает True, если имя подходит условиям, иначе - False."""
        if not isinstance(username, str):
            raise TypeError(f"Expected type \"str\", got {type(username)} instead")

        if len(username) < 2:
            return False

        return True

    @staticmethod
    def check_name_uniqueness(username):
        """Проверяет имя пользователя, возвращает True, если имя уникально, иначе - False."""
        users = fileProvider.FileProvider.get_users()
        for user in users:
            if username == user.name or username == "Администратор":
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
        if len(answer) == 0:
            return False
        return True

class User:
    """Класс User описывает пользователя."""
    def __init__(self, name, password: str):
        """Устанавливает все необходимые атрибуты для объекта User."""
        self.name = name
        self.password = password

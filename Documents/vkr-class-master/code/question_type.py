from enum import IntEnum


class QuestionType(IntEnum):
    """Класс QuestionType, наследник класса IntEnum- перечисление для типов вопроса."""
    base = 0,
    radio_button = 1,
    check_button = 2

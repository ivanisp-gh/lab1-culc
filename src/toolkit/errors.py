class ToolkitError(Exception):
    pass


class DivisionByZeroError(ToolkitError):
    """Деление на ноль."""
    pass



class NegativeDistanceError(ToolkitError):
    """Отрицательное расстояние."""
    pass


class BelowAbsoluteZeroError(ToolkitError):
    """Ниже абсолютного нуля."""
    pass




class ValidationError(ToolkitError):
    """Некорректные входные данные."""
    pass



class ValueTooLargeError(ToolkitError):
    """Ошибка памяти, значение слишком велико"""
    pass
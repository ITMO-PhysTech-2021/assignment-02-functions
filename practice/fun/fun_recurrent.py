from typing import Callable, Any


def __recurrent(
        n: Any,
        stop_condition: Callable[[Any], bool],
        transform: Callable[[Any], Any],
        value: Callable[[Any], Any]
) -> Any:
    """Это вспомогательная функция, не надо ее менять"""
    if stop_condition(n):
        return n
    return __recurrent(transform(n), stop_condition, transform, value) + value(n)


def identity(n):
    """Вернуть число n, используя __recurrent"""
    return __recurrent(
        n,
        lambda x: x == 0,
        Ellipsis,
        Ellipsis
    )


def log2(n):
    """Вернуть округленный вниз двоичный логарифм n, используя __recurrent"""
    return __recurrent(
        n,
        lambda x: x == 1,
        Ellipsis,
        Ellipsis
    )


def push(n):
    """Вернуть массив, в котором единственное число 0 лежит на глубине n"""

    def _depth(item):
        """Вернуть глубину вложенного массива item"""
        pass

    return __recurrent(
        n,
        Ellipsis,
        Ellipsis,
        Ellipsis
    )

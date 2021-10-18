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
        stop_condition=lambda x: x == 0,
        transform=Ellipsis,
        value=Ellipsis
    )


def log2(n):
    """Вернуть округленный вниз двоичный логарифм n, используя __recurrent"""
    return __recurrent(
        n,
        stop_condition=Ellipsis,
        transform=Ellipsis,
        value=Ellipsis
    )


def push(n):
    """Вернуть массив, в котором единственное число 0 лежит на глубине n"""

    def __depth(item):
        """Вернуть глубину вложенного массива item"""
        pass

    return __recurrent(
        n,
        stop_condition=Ellipsis,
        transform=Ellipsis,
        value=Ellipsis
    )

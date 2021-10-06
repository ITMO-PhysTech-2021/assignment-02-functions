def tokenize(expr):
    """Вернуть строку, разбитую на токены"""
    pass


def parse(tokens):
    """Вернуть значение выражения"""
    pointer = 0

    def _parse_atom():
        """Вернуть преобразованное в число значение tokens[pointer]"""
        nonlocal pointer
        pass

    def _parse_term():
        """Вернуть значение произведения/частного, начинающегося в tokens[pointer]"""
        nonlocal pointer
        pass

    def _parse_expression():
        """Вернуть значение выражения, начинающегося в tokens[pointer]"""
        nonlocal pointer
        pass

    return _parse_expression()

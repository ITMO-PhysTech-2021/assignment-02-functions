from typing import Callable, List, Any, Optional


def visualize(
        trace_args: Optional[List[str]] = None
):
    if trace_args is None:
        trace_args = []

    def decorator(function: Callable[[Any], Any]):
        depth = 0

        def __tracer(*args, **kwargs):
            nonlocal depth
            selection = list(map(lambda name: f'{name}={kwargs.get(name, None)}', trace_args))
            print(f'{"  " * depth}{function.__name__}({", ".join(selection)})')
            depth += 1
            result = function(*args, **kwargs)
            depth -= 1
            print(f'{"  " * depth}-> {result}')
            return result

        return __tracer

    return decorator

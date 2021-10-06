from typing import Callable, Optional, List, Any, Dict
from pytest import fail
from copy import deepcopy
from io import StringIO


def CTEST(
        function: Callable,
        input_args: List[Any], output: Any,
        input_kwargs: Optional[Dict[str, Any]] = None
):
    if input_kwargs is None:
        input_kwargs = dict()
    input_copy = deepcopy(input_args)
    assert function(*input_args, **input_kwargs) == output
    assert input_args == input_copy


def PTEST(
        function: Callable,
        input_args: List[Any], output: str,
        input_kwargs: Optional[Dict[str, Any]] = None,
        call_limit: Optional[int] = None, redirect_input: bool = False
):
    if input_kwargs is None:
        input_kwargs = dict()
    args, kwargs = input_args, input_kwargs
    if redirect_input:
        assert all(map(lambda item: type(item) is str, input_args))
        args, kwargs = [], {'input': Input(input_args)}
    printer = Print(call_limit)
    kwargs['print'] = printer
    function(*args, **kwargs)
    assert printer.get() == output


class Input:
    def __init__(self, data: List[str], expect_prompt: Optional[str] = None):
        self.data: List[str] = []
        self.expect_prompt: Optional[int] = None
        self.calls = 0
        self.setup(data, expect_prompt)

    def setup(self, data: List[str], expect_prompt: Optional[str]):
        self.calls = 0
        self.data = data
        self.expect_prompt = expect_prompt

    def __call__(self, *args, **kwargs):
        if self.expect_prompt is None:
            assert len(args) + len(kwargs) == 0
            return

        assert len(args) + len(kwargs) == 1
        if len(args) > 0:
            assert args[0] == self.expect_prompt
        else:
            assert kwargs.keys()[0] == 'prompt'
            assert kwargs['prompt'] == self.expect_prompt

        assert self.calls < len(self.data)
        self.calls += 1
        return self.data[self.calls - 1]


class Print:
    def __init__(self, call_limit: Optional[int] = None):
        self.call_limit: Optional[int] = None
        self.stream: Optional[StringIO] = None
        self.calls = 0
        self.setup(call_limit)

    def setup(self, call_limit: Optional[int]):
        self.call_limit = call_limit
        self.stream = StringIO()
        self.calls = 0

    def __call__(self, *args, **kwargs):
        assert 'file' not in kwargs.keys()
        kwargs['file'] = self.stream
        self.calls += 1
        if self.call_limit is not None:
            assert self.calls <= self.call_limit
        print(*args, **kwargs)

    def get(self):
        return self.stream.getvalue().rstrip()

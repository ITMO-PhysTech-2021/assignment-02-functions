import fun_args
from pytest import mark
from common.test_utils import CTEST, PTEST


# @formatter:off
@mark.parametrize(
    ['input_args', 'input_kwargs', 'output'],
    [
        ([ 0, 1, 2 ], { 'mode': 'args' }, '0 1 2'),
        ([ 0, 1, 2 ], { 'mode': 'list' }, '[0, 1, 2]'),
        ([ 0, 1, 2 ], { 'mode': 'len' }, '3'),
        ([ ], { 'mode': 'args' }, ''),
        ([ ], { 'mode': 'list' }, '[]'),
        ([ ], { 'mode': 'len' }, '0'),
        ([ -1 ], { 'mode': 'args' }, '-1'),
        ([ -1 ], { 'mode': 'list' }, '[-1]'),
        ([ -1 ], { 'mode': 'len' }, '1'),
    ]
)
# @formatter:on
def test_log_args(input_args, input_kwargs, output):
    PTEST(fun_args.log_args, input_args, output, input_kwargs=input_kwargs)


# @formatter:off
@mark.parametrize(
    ['input_args', 'input_kwargs', 'output'],
    [

    ]
)
# @formatter:on
def test_smart_filter(input_args, input_kwargs, output):
    CTEST(fun_args.smart_filter, input_args, output, input_kwargs=input_kwargs)


# @formatter:off
@mark.parametrize(
    ['input_args', 'input_kwargs', 'output'],
    [

    ]
)
# @formatter:on
def test_smart_map(input_args, input_kwargs, output):
    CTEST(fun_args.smart_map, input_args, output)

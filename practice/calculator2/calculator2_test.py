import calculator2
from pytest import mark
from common.test_utils import CTEST


# @formatter:off
@mark.parametrize(
    ['input_args', 'output'],
    [
        ([ '2 + 2' ], 4),
        ([ '-1 + 20 / 4' ], 4),
        ([ '1 + 2 * 3 / 4 + 5' ], 7),
        ([ '44 / 11 * 2 + 44 / 2 / 2' ], 19),
        ([ '0' ], 0),
        ([ '2 + -1 * 10 / 10 - -3 / 6' ], 2),
        ([ '-1 / -1 * 2' ], 2),
        ([ '10 * 2 + 3 / 4' ], 20),
        ([ '49 - 40 * 41 / 2 / 2 / -5 / 2 + 999 - 100 * 10' ], 89),
        ([ '2 - 2 - 2' ], -2)
    ]
)
# @formatter:on
def test_calculator2_manual(input_args, output):
    def __process(expr):
        return calculator2.parse(calculator2.tokenize(expr))

    CTEST(__process, input_args, output)

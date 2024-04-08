import pytest
from src.leetcode.easy.palindrome_number import solution_1, solution_2


@pytest.mark.parametrize(
    "x,expected",
    [
        (541, False),
        (545, True),
        (5455, False),
        (55455, True),
    ],
)
def test_solution_1(x, expected):
    assert solution_1(x) == expected


@pytest.mark.parametrize(
    "x,expected",
    [
        (541, False),
        (545, True),
        (5455, False),
        (55455, True),
    ],
)
def test_solution_2(x, expected):
    assert solution_2(x) == expected

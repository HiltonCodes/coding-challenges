import pytest
from src.leetcode.easy.roman_to_integer import solution_1, solution_2


@pytest.mark.parametrize(
    "numeral,expected",
    [
        ("II", 2),
        ("XII", 12),
        ("XXVII", 27),
        ("IV", 4),
        ("IX", 9),
        ("XL", 40),
        ("XC", 90),
        ("CLXVII", 167),
        ("CLXIX", 169),
        ("CD", 400),
        ("CM", 900),
    ],
)
def test_solution_1(numeral, expected):
    assert solution_1(numeral) == expected


@pytest.mark.parametrize(
    "numeral,expected",
    [
        ("II", 2),
        ("XII", 12),
        ("XXVII", 27),
        ("IV", 4),
        ("IX", 9),
        ("XL", 40),
        ("XC", 90),
        ("CLXVII", 167),
        ("CLXIX", 169),
        ("CD", 400),
        ("CM", 900),
    ],
)
def test_solution_2(numeral, expected):
    assert solution_2(numeral) == expected

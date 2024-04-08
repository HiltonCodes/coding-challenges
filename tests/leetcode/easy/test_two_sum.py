import pytest
from src.leetcode.easy.two_sum import solution_1, solution_2


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([7, 11, 16, 12, 15, 2, 9, 92], 9, [0, 5]),
        ([32, 104, 16, 12, 15, 2, 9, 92, 1, 8, 67], 20, [3, 9]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ],
)
def test_solution_1(nums, target, expected):
    actual = solution_1(nums, target)

    assert sorted(actual) == expected


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([7, 11, 16, 12, 15, 2, 9, 92], 9, [0, 5]),
        ([32, 104, 16, 12, 15, 2, 9, 92, 1, 8, 67], 20, [3, 9]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ],
)
def test_solution_2(nums, target, expected):
    actual = solution_2(nums, target)

    assert sorted(actual) == expected

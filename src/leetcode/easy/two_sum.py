"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.


Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""


def solution_1(nums: list[int], target: int) -> list[int]:
    """The most obvious solution is to:

    - Start with the first number, and compare that to every subsequent number. Test each pair to see if they add up to the target.
    - If no matches after comparing the first number with every other number, move on to the second number and compare those.
    - Repeat this until we get to the end of the list.

    This is super slow, there is a better way - see solution_2.
    """

    length = len(nums)
    for i in range(0, length):
        num_1 = nums[i]

        for j in range(i + 1, length):
            num_2 = nums[j]

            if num_1 + num_2 == target:
                return [i, j]

    raise ValueError("No solution found!")


def solution_2(nums: list[int], target: int) -> list[int]:
    """A more optimal way is to cache the required number as you iterate through.

    - Consider the list [10, 15, 18, 6, 8, 12] and a target of 21.
    - Start at the beginning of the list -> I see a 10
        - therefore I know if I encounter an 11 later on, I have a match.
        - move on to 15 -> I know if I encounter a 6 later on, I have a match.
        - move on to 18 -> I know if I have a 3 later on, I have a match.
    - Thus if we store the required values as we progress through the list, we can find a solution in a single loop.
    """
    cache: dict[int, int] = {}

    for i, num in enumerate(nums):
        if num in cache:
            return [cache[num], i]

        cache[target - num] = i

    raise ValueError("No solution found!")


if __name__ == "__main__":
    nums, target, expected = [11, 2, 15, 7, 4, 8], 9, [1, 3]

    solution_2(nums, target)

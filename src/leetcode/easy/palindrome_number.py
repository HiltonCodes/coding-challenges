"""
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Constraints:

-231 <= x <= 231 - 1

Follow up: Could you solve it without converting the integer to a string?
"""


def solution_1(x: int) -> bool:
    """The most simple solution is to convert the number to a string, and then compare the string to the reversed string."""
    as_str = str(x)

    return as_str == as_str[::-1]


def solution_2(x: int) -> bool:
    """If we do not allow ourselves to cover the integer to a string, it is slightly more difficult.
    - Create a variable tmp equal to x.
    - Use the % operator to get the last digit of x, and the // operator to cut off the last digit of tmp. Put this in a while loop and we can progressively create the reverse of x.
    """
    tmp = x
    ans = 0

    while tmp > 0:
        remainder = tmp % 10
        tmp //= 10
        ans = (ans * 10) + remainder

    return ans == x


if __name__ == "__main__":
    x = 683398

    solution_2(x)

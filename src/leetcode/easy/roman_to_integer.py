"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.



Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""

MAIN_VALUES = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
SECONDARY_VALUES = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
SECONDARY_VALUE_REPLACEMENTS = {"IV": "IIII", "IX": "VIIII", "XL": "XXXX", "XC": "LXXXX", "CD": "CCCC", "CM": "DCCCC"}


def solution_1(numerals: str) -> int:
    """
    This is a fairly simple one. We start at the first numeral, and add up the result as we iterate through them. We need to sometimes increment the pointer by 2 (for the cases of IV, IX, etc), and sometimes increment the pointer by 1 (for the cases of I, V, etc). We just use a dict to store the values and look them up.
    """
    result = 0
    last_index = len(numerals) - 1

    i = 0
    while i <= last_index:
        part = numerals[i]

        if i == last_index:
            return result + MAIN_VALUES[part]

        next_part = numerals[i + 1]

        secondary_value = SECONDARY_VALUES.get(part + next_part)

        if secondary_value:
            result += secondary_value
            i += 2
        else:
            main_value = MAIN_VALUES[part]
            result += main_value
            i += 1

    return result


def solution_2(numerals: str) -> int:
    """
    In solution 1, we looked up the hash table lots. We can just use a different approach, since ultimately any of the SECONDARY_VALUES can be replaced with the MAIN_VALUES, so we have a replaced value that only contain the MAIN_VALUES.
    """
    replaced = numerals
    for i, v in SECONDARY_VALUE_REPLACEMENTS.items():
        replaced = replaced.replace(i, v)

    result = 0

    for part in replaced:
        result += MAIN_VALUES[part]

    return result

"""
1903. Largest Odd Number in String (Easy)

You are given a string `num` representing a large integer. Return the **largest odd integer** (as a string) 
that is a **non-empty substring** of `num`, or an empty string if no such integer exists.

A **substring** is a contiguous sequence of characters within a string.

Example 1:
Input: num = "52"
Output: "5"

Example 2:
Input: num = "4206"
Output: ""

Example 3:
Input: num = "35427"
Output: "35427"

Constraints:
- 1 <= num.length <= 100
- num only consists of digits and does not contain leading zeros.
"""

import unittest

"""
Approach:
We can check the string from right to left, looking for the first odd digit. 
We will then return the substring from the beginning of the string up to that index. 
If no odd number is found, return an empty string.
"""

class Solution:
    def largestOddNumber(self, num: str) -> str:
        pass

class TestLargestOddNumber(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        num = "52"
        self.assertEqual(self.solution.largestOddNumber(num), "5")

    def test_example_2(self):
        num = "4206"
        self.assertEqual(self.solution.largestOddNumber(num), "")

    def test_example_3(self):
        num = "35427"
        self.assertEqual(self.solution.largestOddNumber(num), "35427")

    def test_single_digit_odd(self):
        num = "7"
        self.assertEqual(self.solution.largestOddNumber(num), "7")

    def test_single_digit_even(self):
        num = "4"
        self.assertEqual(self.solution.largestOddNumber(num), "")

if __name__ == "__main__":
    unittest.main()

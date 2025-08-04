"""
367. Valid Perfect Square (Easy)

Given a positive integer num, write a function which returns True if num is a perfect square or False otherwise.

A perfect square is an integer that is the square of another integer.

Example 1:
Input: num = 16
Output: true

Example 2:
Input: num = 14
Output: false

Constraints:
- 1 <= num <= 2³¹ - 1
"""

from typing import List
import unittest

"""
Approach:
We can use binary search to find the square root of the number. If we find an integer whose square is equal to num, 
then it is a perfect square.
"""

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        pass

class TestValidPerfectSquare(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        num = 16
        self.assertTrue(self.solution.isPerfectSquare(num))

    def test_example_2(self):
        num = 14
        self.assertFalse(self.solution.isPerfectSquare(num))

    def test_single_square(self):
        num = 1
        self.assertTrue(self.solution.isPerfectSquare(num))

    def test_large_square(self):
        num = 100000000
        self.assertTrue(self.solution.isPerfectSquare(num))

    def test_not_square(self):
        num = 123456
        self.assertFalse(self.solution.isPerfectSquare(num))

if __name__ == "__main__":
    unittest.main()

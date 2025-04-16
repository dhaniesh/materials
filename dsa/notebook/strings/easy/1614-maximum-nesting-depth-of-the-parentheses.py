"""
1614. Maximum Nesting Depth of the Parentheses (Easy)

A string is a valid parentheses string if it is non-empty, and it consists of pairs of parentheses 
in which each opening parenthesis '(' is followed by a closing parenthesis ')'.

Given a valid parentheses string s, return the **maximum** depth of nesting of the parentheses 
in s.

Example 1:
Input: s = "(1+(2*3)+((8)/4))+1"
Output: 3

Example 2:
Input: s = "(1)+((2))+(((3)))"
Output: 3

Constraints:
- 1 <= s.length <= 100
- s consists of digits, '+', '-', '*', '/', '(', and ')'.
- It is guaranteed that the parentheses in s are balanced.
"""

import unittest

"""
Approach:
We can use a counter to track the depth of parentheses. 
Each time we encounter an opening parenthesis, we increase the depth, 
and each time we encounter a closing parenthesis, we decrease it. 
We keep track of the maximum depth encountered.
"""

class Solution:
    def maxDepth(self, s: str) -> int:
        pass

class TestMaximumNestingDepth(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        s = "(1+(2*3)+((8)/4))+1"
        self.assertEqual(self.solution.maxDepth(s), 3)

    def test_example_2(self):
        s = "(1)+((2))+(((3)))"
        self.assertEqual(self.solution.maxDepth(s), 3)

    def test_single_parenthesis(self):
        s = "(1)"
        self.assertEqual(self.solution.maxDepth(s), 1)

    def test_no_parentheses(self):
        s = "12345"
        self.assertEqual(self.solution.maxDepth(s), 0)

    def test_nested_parentheses(self):
        s = "((((((()))))))"
        self.assertEqual(self.solution.maxDepth(s), 6)

if __name__ == "__main__":
    unittest.main()


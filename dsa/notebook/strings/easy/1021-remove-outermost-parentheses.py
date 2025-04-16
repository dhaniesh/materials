"""
1021. Remove Outermost Parentheses (Easy)

A valid parentheses string is a non-empty string that consists of opening and closing parentheses 
in the correct order.

In a valid parentheses string, every opening parenthesis has a corresponding closing parenthesis 
and each pair of parentheses are properly nested.

Given a valid parentheses string s, return a new string after removing the outermost parentheses of every 
valid parentheses string in s.

Example 1:
Input: s = "(()())"
Output: "()()"

Example 2:
Input: s = "(()())(())"
Output: "()()()"

Example 3:
Input: s = "()()"
Output: ""

Constraints:
- 1 <= s.length <= 1000
- s[i] is either '(' or ')'
- s is a valid parentheses string.
"""

import unittest

"""
Approach:
We can use a counter to keep track of the balance between the opening and closing parentheses. 
Once we encounter a balanced pair, we can omit the outermost parentheses and add the remaining string.
"""

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        pass

class TestRemoveOutermostParentheses(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        s = "(()())"
        self.assertEqual(self.solution.removeOuterParentheses(s), "()()")

    def test_example_2(self):
        s = "(()())(())"
        self.assertEqual(self.solution.removeOuterParentheses(s), "()()()")

    def test_example_3(self):
        s = "()()"
        self.assertEqual(self.solution.removeOuterParentheses(s), "")

    def test_single_pair(self):
        s = "()"
        self.assertEqual(self.solution.removeOuterParentheses(s), "")

    def test_long_string(self):
        s = "(((())))"
        self.assertEqual(self.solution.removeOuterParentheses(s), "(()())")

if __name__ == "__main__":
    unittest.main()

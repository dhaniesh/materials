"""
678. Valid Parenthesis String (Medium)

Given a string s containing only three types of characters: '(', ')' and '*',
return true if s is valid.

A string is valid if:
- Open parentheses must be closed by the same type of parentheses.
- Open parentheses must be closed in the correct order.
- '*' can be treated as '(', ')' or an empty string.
"""

import unittest

class Solution:
    def checkValidString(self, s: str) -> bool:
        mn, mx = 0, 0
        for c in s:
            if c == '(':
                mn += 1; mx += 1
            elif c == ')':
                mn -= 1; mx -= 1
            else:
                mn -= 1; mx += 1
            if mn < 0:
                mn = 0
            if mx < 0:
                return False
        return mn == 0


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        s = "()"
        self.assertTrue(self.sol.checkValidString(s))

    def test_example_2(self):
        s = "(*)"
        self.assertTrue(self.sol.checkValidString(s))

    def test_example_3(self):
        s = "(*))"
        self.assertTrue(self.sol.checkValidString(s))

    def test_invalid_case(self):
        s = "((*"
        self.assertFalse(self.sol.checkValidString(s))

    def test_empty_string(self):
        s = ""
        self.assertTrue(self.sol.checkValidString(s))

    def test_all_stars(self):
        s = "***"
        self.assertTrue(self.sol.checkValidString(s))

    def test_nested(self):
        s = "(*()"
        self.assertTrue(self.sol.checkValidString(s))


if __name__ == '__main__':
    unittest.main()

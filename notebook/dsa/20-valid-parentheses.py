"""
🧩 Problem: Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:
1. Open brackets are closed by the same type of brackets.
2. Open brackets are closed in the correct order.
3. Every closing bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Constraints:
• 1 <= s.length <= 10⁴
• s consists of parentheses only '()[]{}'.

Approach:
- Use a stack to keep track of opening brackets.
- For each closing bracket, check if the top of the stack is the matching opening one.
- Return True if the stack is empty at the end.
"""

import unittest

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {")": "(", "}": "{", "]": "["}
        for c in s:
            if c in pair:
                if stack and stack[-1] == pair[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack


class TestValidParentheses(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertTrue(self.solution.isValid("()"))

    def test_example_2(self):
        self.assertTrue(self.solution.isValid("()[]{}"))

    def test_example_3(self):
        self.assertFalse(self.solution.isValid("(]"))

    def test_nested_valid(self):
        self.assertTrue(self.solution.isValid("{[()]}"))

    def test_unmatched_open(self):
        self.assertFalse(self.solution.isValid("((("))

    def test_unmatched_close(self):
        self.assertFalse(self.solution.isValid("()))"))

    def test_mixed_invalid(self):
        self.assertFalse(self.solution.isValid("{[}]"))

    def test_empty_string(self):
        self.assertTrue(self.solution.isValid(""))

    def test_long_valid_sequence(self):
        s = "({[]})" * 1000
        self.assertTrue(self.solution.isValid(s))

    def test_long_invalid_sequence(self):
        s = "({[)]}" * 1000
        self.assertFalse(self.solution.isValid(s))


if __name__ == "__main__":
    unittest.main()

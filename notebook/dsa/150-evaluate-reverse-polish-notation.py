"""
Title: Evaluate Reverse Polish Notation

Problem Statement:
You are given an array of strings `tokens` that represents an arithmetic expression in Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Valid operators are '+', '-', '*', and '/'. Each operand may be an integer or another expression.
Note that division between two integers should truncate toward zero.

Example 1:
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22

Approach:
Use a stack to evaluate the Reverse Polish expression:
- For each token:
    - If it’s a number, push it to the stack.
    - If it’s an operator, pop the last two numbers and apply the operation.
- The final value in the stack is the result.
"""

from typing import List
import unittest


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in ("+", "-", "*", "/"):
                stack.append(int(token))
                continue

            b = stack.pop()
            a = stack.pop()

            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                # Use int() to truncate toward zero
                stack.append(int(a / b))

        return stack[0]


class TestEvalRPN(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.evalRPN(["2", "1", "+", "3", "*"]), 9)

    def test_example_2(self):
        self.assertEqual(self.solution.evalRPN(["4", "13", "5", "/", "+"]), 6)

    def test_example_3(self):
        self.assertEqual(
            self.solution.evalRPN(
                ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
            ),
            22,
        )

    def test_negative_result(self):
        self.assertEqual(self.solution.evalRPN(["2", "3", "-"]), -1)

    def test_division_truncation(self):
        # Division should truncate toward zero
        self.assertEqual(self.solution.evalRPN(["7", "3", "/"]), 2)
        self.assertEqual(self.solution.evalRPN(["-7", "3", "/"]), -2)


if __name__ == "__main__":
    unittest.main()

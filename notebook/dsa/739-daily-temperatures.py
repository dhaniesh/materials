"""
739. Daily Temperatures

Problem Statement:
Given a list of daily temperatures `temperatures`, return a list `answer` such that
`answer[i]` is the number of days you have to wait after the i-th day to get a warmer temperature.
If there is no future day for which this is possible, keep `answer[i] == 0`.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]

Constraints:
- 1 <= len(temperatures) <= 10^5
- 30 <= temperatures[i] <= 100

Approach:
Traverse the temperature list backward, maintaining a monotonic decreasing stack
of (temperature, index). For each day, pop all cooler or equal temperatures from the stack.
If a warmer day remains, compute the index difference; otherwise, set 0.
Time complexity: O(n)
Space complexity: O(n)
"""

from typing import List
import unittest

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []  # (temperature, index)
        for index in range(len(temperatures)-1, -1, -1):
            temperature = temperatures[index]
            while stack and stack[-1][0] <= temperature:
                stack.pop()
            if stack:
                answer[index] = stack[-1][1] - index
            stack.append((temperature, index))
        return answer


class TestDailyTemperatures(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_case(self):
        self.assertEqual(
            self.sol.dailyTemperatures([73,74,75,71,69,72,76,73]),
            [1,1,4,2,1,1,0,0]
        )

    def test_increasing_temperatures(self):
        self.assertEqual(
            self.sol.dailyTemperatures([30,40,50,60]),
            [1,1,1,0]
        )

    def test_decreasing_temperatures(self):
        self.assertEqual(
            self.sol.dailyTemperatures([90,80,70,60]),
            [0,0,0,0]
        )

    def test_equal_temperatures(self):
        self.assertEqual(
            self.sol.dailyTemperatures([70,70,70]),
            [0,0,0]
        )

    def test_single_element(self):
        self.assertEqual(
            self.sol.dailyTemperatures([75]),
            [0]
        )

    def test_two_elements(self):
        self.assertEqual(
            self.sol.dailyTemperatures([70,75]),
            [1,0]
        )
        self.assertEqual(
            self.sol.dailyTemperatures([80,75]),
            [0,0]
        )


if __name__ == "__main__":
    unittest.main()

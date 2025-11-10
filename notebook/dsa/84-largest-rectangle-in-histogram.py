"""
84: Largest Rectangle in Histogram

Problem:
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1,
return the area of the largest rectangle in the histogram.

Example 1:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The largest rectangle is 5x2 = 10.

Example 2:
Input: heights = [2,4]
Output: 4
Explanation: The largest rectangle is 2x2 = 4.

Constraints:
1 <= heights.length <= 10^5
0 <= heights[i] <= 10^4

Approach:
- Use a monotonic increasing stack to keep track of bars' indices and heights.
- When encountering a bar lower than the stack's top height, pop from the stack and calculate the area
  with the popped height as the smallest height.
- Compute the remaining possible areas after the loop.
- Time complexity: O(n)
- Space complexity: O(n)
"""

from typing import List
import unittest

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # pair: (index, height)
        max_area = 0

        for i, height in enumerate(heights):
            start = i  # current start
            while stack and height < stack[-1][-1]:
                j, h = stack.pop()
                w = i - j
                max_area = max(max_area, h * w)
                start = j  # to get track of previous extensions
            stack.append((start, height))

        for i, height in stack:
            max_area = max(max_area, height * (len(heights) - i))
        return max_area


class TestLargestRectangleArea(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_case_1(self):
        self.assertEqual(self.sol.largestRectangleArea([2,1,5,6,2,3]), 10)

    def test_example_case_2(self):
        self.assertEqual(self.sol.largestRectangleArea([2,4]), 4)

    def test_all_equal_heights(self):
        self.assertEqual(self.sol.largestRectangleArea([3,3,3,3]), 12)

    def test_strictly_increasing(self):
        self.assertEqual(self.sol.largestRectangleArea([1,2,3,4,5]), 9)

    def test_strictly_decreasing(self):
        self.assertEqual(self.sol.largestRectangleArea([5,4,3,2,1]), 9)

    def test_single_bar(self):
        self.assertEqual(self.sol.largestRectangleArea([7]), 7)

    def test_with_zeros(self):
        self.assertEqual(self.sol.largestRectangleArea([0,0,0]), 0)

    def test_mixed_with_zero(self):
        self.assertEqual(self.sol.largestRectangleArea([2,0,2]), 2)

    def test_large_case(self):
        heights = [10000] * 1000
        self.assertEqual(self.sol.largestRectangleArea(heights), 10000 * 1000)


if __name__ == "__main__":
    unittest.main()


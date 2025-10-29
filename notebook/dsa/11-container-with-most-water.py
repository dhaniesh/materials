"""
Title: Container With Most Water

Problem Statement:
You are given an integer array height of length n. There are n vertical lines drawn such that
the two endpoints of the i-th line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container that holds the most water.
Return the maximum amount of water a container can store.

Note: You may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The maximum area of water (between index 1 and 8) is 49.

Example 2:
Input: height = [1,1]
Output: 1

Constraints:
- n == height.length
- 2 <= n <= 10^5
- 0 <= height[i] <= 10^4

Approach:
1. Use two pointers, one at the start (l) and one at the end (r).
2. Calculate the area between l and r as:
       area = min(height[l], height[r]) * (r - l)
3. Keep track of the maximum area encountered.
4. Move the pointer corresponding to the smaller height inward,
   because increasing the smaller line might increase the area.
5. Continue until l and r meet.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List
import unittest

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        l, r = 0, len(height) - 1
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            max_area = max(max_area, area)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return max_area


class TestMaxArea(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        expected = 49
        self.assertEqual(self.solution.maxArea(height), expected)

    def test_example_2(self):
        height = [1, 1]
        expected = 1
        self.assertEqual(self.solution.maxArea(height), expected)

    def test_increasing_heights(self):
        height = [1, 2, 3, 4, 5]
        expected = 6  # Between lines at indices 1 and 4 (2 * 3)
        self.assertEqual(self.solution.maxArea(height), expected)

    def test_decreasing_heights(self):
        height = [5, 4, 3, 2, 1]
        expected = 6  # Between lines at indices 0 and 3 (3 * 2)
        self.assertEqual(self.solution.maxArea(height), expected)

    def test_all_same_height(self):
        height = [4, 4, 4, 4, 4]
        expected = 16  # Between first and last line (4 * 4)
        self.assertEqual(self.solution.maxArea(height), expected)

    def test_small_input(self):
        height = [1, 2]
        expected = 1
        self.assertEqual(self.solution.maxArea(height), expected)


if __name__ == "__main__":
    unittest.main()

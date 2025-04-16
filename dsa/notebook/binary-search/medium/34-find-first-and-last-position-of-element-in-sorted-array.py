"""
34. Find First and Last Position of Element in Sorted Array (Medium)

Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value.

If `target` is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]

Constraints:
- 0 <= nums.length <= 10⁵
- -10⁹ <= nums[i] <= 10⁹
- `nums` is a non-decreasing array.
- -10⁹ <= target <= 10⁹
"""

from typing import List
import unittest

"""
Approach:


"""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        pass

class TestSearchRange(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [5, 7, 7, 8, 8, 10]
        target = 8
        self.assertEqual(self.solution.searchRange(nums, target), [3, 4])

    def test_example_2(self):
        nums = [5, 7, 7, 8, 8, 10]
        target = 6
        self.assertEqual(self.solution.searchRange(nums, target), [-1, -1])

    def test_example_3(self):
        nums = []
        target = 0
        self.assertEqual(self.solution.searchRange(nums, target), [-1, -1])

    def test_single_element_match(self):
        nums = [5]
        target = 5
        self.assertEqual(self.solution.searchRange(nums, target), [0, 0])

    def test_single_element_no_match(self):
        nums = [5]
        target = 1
        self.assertEqual(self.solution.searchRange(nums, target), [-1, -1])

if __name__ == "__main__":
    unittest.main()

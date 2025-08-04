"""
704. Binary Search

Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, 
write a function to search `target` in `nums`. If `target` exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1

Constraints:
- 1 <= nums.length <= 10⁴
- -10⁴ < nums[i], target < 10⁴
- All the integers in `nums` are unique.
- `nums` is sorted in ascending order.
"""

from typing import List
import unittest

"""
Approach:


"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pass

class TestBinarySearch(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [-1, 0, 3, 5, 9, 12]
        target = 9
        result = self.solution.search(nums, target)
        self.assertEqual(result, 4)

    def test_example_2(self):
        nums = [-1, 0, 3, 5, 9, 12]
        target = 2
        result = self.solution.search(nums, target)
        self.assertEqual(result, -1)

    def test_first_element(self):
        nums = [1, 2, 3, 4, 5]
        target = 1
        result = self.solution.search(nums, target)
        self.assertEqual(result, 0)

    def test_last_element(self):
        nums = [10, 20, 30, 40, 50]
        target = 50
        result = self.solution.search(nums, target)
        self.assertEqual(result, 4)

    def test_not_found(self):
        nums = [100, 200, 300]
        target = 150
        result = self.solution.search(nums, target)
        self.assertEqual(result, -1)

if __name__ == "__main__":
    unittest.main()

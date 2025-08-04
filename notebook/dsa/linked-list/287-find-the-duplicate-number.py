"""
287. Find the Duplicate Number (Medium)

Given an array of integers, find the duplicate number. You must solve it in O(n) time complexity.

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3
"""

import unittest

"""
Approach:
We will use Floyd's Tortoise and Hare (Cycle Detection) algorithm to find the duplicate in O(n) time and O(1) space.
"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        pass

class TestFindDuplicateNumber(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [1, 3, 4, 2, 2]
        result = self.solution.findDuplicate(nums)
        self.assertEqual(result, 2)

    def test_example_2(self):
        nums = [3, 1, 3, 4, 2]
        result = self.solution.findDuplicate(nums)
        self.assertEqual(result, 3)

if __name__ == "__main__":
    unittest.main()

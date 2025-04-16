"""
15. 3Sum

Given an integer array `nums`, return all the triplets [nums[i], nums[j], nums[k]] such that:
- 0 <= i < j < k < nums.length
- nums[i] + nums[j] + nums[k] == 0

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:
Input: nums = []
Output: []

Example 3:
Input: nums = [0]
Output: []

Constraints:
- 0 <= nums.length <= 3000
- -10⁵ <= nums[i] <= 10⁵
"""

from typing import List
import unittest

"""
Approach:


"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pass

class TestThreeSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [-1, 0, 1, 2, -1, -4]
        result = self.solution.threeSum(nums)
        self.assertEqual(result, [[-1, -1, 2], [-1, 0, 1]])

    def test_example_2(self):
        nums = []
        result = self.solution.threeSum(nums)
        self.assertEqual(result, [])

    def test_example_3(self):
        nums = [0]
        result = self.solution.threeSum(nums)
        self.assertEqual(result, [])

    def test_no_triplets(self):
        nums = [1, 2, 3, 4]
        result = self.solution.threeSum(nums)
        self.assertEqual(result, [])

    def test_all_negatives(self):
        nums = [-1, -2, -3, -4]
        result = self.solution.threeSum(nums)
        self.assertEqual(result, [])

if __name__ == "__main__":
    unittest.main()

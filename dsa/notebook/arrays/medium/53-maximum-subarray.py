"""
53. Maximum Subarray

Given an integer array `nums`, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
Input: nums = [1]
Output: 1

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23

Constraints:
- 1 <= nums.length <= 10⁵
- -10⁴ <= nums[i] <= 10⁴

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, 
which is more subtle.
"""

from typing import List
import unittest

"""
Approach:
- if sums goes < 0, make a new subarry
"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        sums = 0
        for num in nums:
            if sums < 0:
                sums = 0
            sums += num
            result = max(result, sums)
        return result



class TestMaximumSubarray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.maxSubArray(
            [-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)

    def test_example_2(self):
        self.assertEqual(self.solution.maxSubArray([1]), 1)

    def test_example_3(self):
        self.assertEqual(self.solution.maxSubArray([5, 4, -1, 7, 8]), 23)

    def test_all_negative(self):
        self.assertEqual(self.solution.maxSubArray([-3, -1, -2]), -1)

    def test_mixed_with_zero(self):
        self.assertEqual(self.solution.maxSubArray([0, -3, 5, -2, 1]), 5)


if __name__ == "__main__":
    unittest.main()

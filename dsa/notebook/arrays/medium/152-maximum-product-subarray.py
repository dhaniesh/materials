"""
152. Maximum Product Subarray

Given an integer array `nums`, find the contiguous subarray (containing at least one number) 
which has the largest product and return its product.

Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product = 6.

Example 2:
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result is 0 because the maximum product is 0, 
        which occurs when the subarray is [0].

Constraints:
- 1 <= nums.length <= 2 * 10⁴
- -10 <= nums[i] <= 10
- The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
"""

from typing import List
import unittest

"""
Approach:


"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pass

class TestMaximumProductSubarray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [2, 3, -2, 4]
        self.assertEqual(self.solution.maxProduct(nums), 6)

    def test_example_2(self):
        nums = [-2, 0, -1]
        self.assertEqual(self.solution.maxProduct(nums), 0)

    def test_all_negative(self):
        nums = [-2, -3, -4]
        self.assertEqual(self.solution.maxProduct(nums), 24)

    def test_single_element(self):
        nums = [-1]
        self.assertEqual(self.solution.maxProduct(nums), -1)

    def test_large_numbers(self):
        nums = [1, 2, 3, 4, 5]
        self.assertEqual(self.solution.maxProduct(nums), 120)

if __name__ == "__main__":
    unittest.main()

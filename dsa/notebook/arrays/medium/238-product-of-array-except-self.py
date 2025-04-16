"""
238. Product of Array Except Self

Given an integer array `nums`, return an array `output` such that `output[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Explanation: The product of elements except self at index 0 is 2 * 3 * 4 = 24.
The product of elements except self at index 1 is 1 * 3 * 4 = 12.
The product of elements except self at index 2 is 1 * 2 * 4 = 8.
The product of elements except self at index 3 is 1 * 2 * 3 = 6.

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
Explanation: The product of elements except self at index 0 is 1 * 0 * -3 * 3 = 0.
The product of elements except self at index 1 is -1 * 0 * -3 * 3 = 0.
The product of elements except self at index 2 is -1 * 1 * -3 * 3 = 9.
The product of elements except self at index 3 is -1 * 1 * 0 * 3 = 0.
The product of elements except self at index 4 is -1 * 1 * -3 * 0 = 0.

Constraints:
- 2 <= nums.length <= 10⁴
- -30 <= nums[i] <= 30
- The answer is guaranteed to fit in a 32-bit integer.
- Do not use the division operator.
"""

from typing import List
import unittest

"""
Approach:


"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pass

class TestProductOfArrayExceptSelf(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [1, 2, 3, 4]
        result = self.solution.productExceptSelf(nums)
        self.assertEqual(result, [24, 12, 8, 6])

    def test_example_2(self):
        nums = [-1, 1, 0, -3, 3]
        result = self.solution.productExceptSelf(nums)
        self.assertEqual(result, [0, 0, 9, 0, 0])

    def test_single_element(self):
        nums = [5]
        result = self.solution.productExceptSelf(nums)
        self.assertEqual(result, [1])

    def test_all_ones(self):
        nums = [1, 1, 1, 1]
        result = self.solution.productExceptSelf(nums)
        self.assertEqual(result, [1, 1, 1, 1])

    def test_mixed_numbers(self):
        nums = [1, 0, -1, 3, -4]
        result = self.solution.productExceptSelf(nums)
        self.assertEqual(result, [0, 0, 0, 0, 0])

if __name__ == "__main__":
    unittest.main()

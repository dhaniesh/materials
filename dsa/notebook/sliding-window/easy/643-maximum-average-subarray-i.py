"""
643. Maximum Average Subarray I (Easy)

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. 
Any answer with a calculation error less than 10⁻⁴ will be accepted.

Example 1:
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: When k is 4, the subarray [12,-5,-6,50] has the maximum average value, which is 12.75.

Example 2:
Input: nums = [5], k = 1
Output: 5.0

Constraints:
- n == nums.length
- 1 <= n <= 10⁵
- -10⁴ <= nums[i] <= 10⁴
- 1 <= k <= n
"""

import unittest

"""
Approach:
We can solve this problem using the sliding window technique. The idea is to calculate the sum of the first 
k elements, and then slide the window by removing the leftmost element and adding the next element, keeping track 
of the maximum sum encountered.
"""

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        pass

class TestMaximumAverageSubarrayI(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [1, 12, -5, -6, 50, 3]
        k = 4
        self.assertEqual(self.solution.findMaxAverage(nums, k), 12.75)

    def test_example_2(self):
        nums = [5]
        k = 1
        self.assertEqual(self.solution.findMaxAverage(nums, k), 5.0)

    def test_large_negative_numbers(self):
        nums = [-1, -2, -3, -4, -5]
        k = 2
        self.assertEqual(self.solution.findMaxAverage(nums, k), -1.5)

    def test_multiple_subarrays(self):
        nums = [1, 2, 3, 4, 5]
        k = 3
        self.assertEqual(self.solution.findMaxAverage(nums, k), 4.0)

    def test_all_elements_are_equal(self):
        nums = [7, 7, 7, 7]
        k = 2
        self.assertEqual(self.solution.findMaxAverage(nums, k), 7.0)

if __name__ == "__main__":
    unittest.main()

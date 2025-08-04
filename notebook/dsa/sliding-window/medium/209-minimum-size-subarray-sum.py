"""
209. Minimum Size Subarray Sum (Medium)

Given an array of positive integers nums and an integer target, return the minimal length of a contiguous subarray 
of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the sum of 7 which is equal to target.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

Constraints:
- 1 <= target <= 10⁹
- 1 <= nums.length <= 10⁵
- 1 <= nums[i] <= 10⁴
"""

import unittest

"""
Approach:
We can use the sliding window (two-pointer) technique to solve this problem in O(n) time. 
The idea is to maintain a window (a range of indices) and adjust it dynamically to find the smallest subarray 
that satisfies the sum condition.
"""

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        pass

class TestMinimumSizeSubarraySum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        target = 7
        nums = [2, 3, 1, 2, 4, 3]
        self.assertEqual(self.solution.minSubArrayLen(target, nums), 2)

    def test_example_2(self):
        target = 4
        nums = [1, 4, 4]
        self.assertEqual(self.solution.minSubArrayLen(target, nums), 1)

    def test_example_3(self):
        target = 11
        nums = [1, 1, 1, 1, 1, 1, 1, 1]
        self.assertEqual(self.solution.minSubArrayLen(target, nums), 0)

    def test_large_target(self):
        target = 15
        nums = [1, 2, 3, 4, 5, 6]
        self.assertEqual(self.solution.minSubArrayLen(target, nums), 5)

    def test_single_element(self):
        target = 5
        nums = [5]
        self.assertEqual(self.solution.minSubArrayLen(target, nums), 1)

if __name__ == "__main__":
    unittest.main()

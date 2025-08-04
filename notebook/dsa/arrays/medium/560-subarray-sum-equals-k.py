"""
560. Subarray Sum Equals K

Given an array of integers `nums` and an integer `k`, return the total number of subarrays whose sum equals to `k`.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2

Constraints:
- 1 <= nums.length <= 2 * 10⁴
- -1000 <= nums[i] <= 1000
- -10⁷ <= k <= 10⁷
"""

from typing import List
import unittest

"""
Approach:
- prefix sum
- calculate how many subarrays can get you the result
"""


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        result = 0
        sum_map = defaultdict(int)
        sum_map[0] = 1  # base prefix
        sums = 0

        for num in nums:
            sums += num
            if sums-k in sum_map:
                result += sum_map[sums-k]
            sum_map[sums] += 1
        return result


class TestSubarraySumEqualsK(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.subarraySum([1, 1, 1], 2), 2)

    def test_example_2(self):
        self.assertEqual(self.solution.subarraySum([1, 2, 3], 3), 2)

    def test_negative_numbers(self):
        self.assertEqual(self.solution.subarraySum([1, -1, 0], 0), 3)

    def test_all_zeros(self):
        self.assertEqual(self.solution.subarraySum([0, 0, 0], 0), 6)

    def test_no_valid_subarray(self):
        self.assertEqual(self.solution.subarraySum([1, 2, 3], 7), 0)


if __name__ == "__main__":
    unittest.main()

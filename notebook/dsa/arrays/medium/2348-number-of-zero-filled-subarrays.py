"""
2348. Number of Zero-Filled Subarrays (Medium)

Given an integer array nums, return the number of subarrays filled with 0.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,3,0,0,2,0,0,4]
Output: 6 
Explanation: 
There are 4 occurrences of [0] as a subarray.
There are 2 occurrences of [0,0] as a subarray.
Total = 6.

Example 2:
Input: nums = [0,0,0,2,0,0]
Output: 9
Explanation: 
There are 5 occurrences of [0] as a subarray.
There are 3 occurrences of [0,0] as a subarray.
There is 1 occurrence of [0,0,0] as a subarray.
Total = 9.

Example 3:
Input: nums = [2,10,2019]
Output: 0

Constraints:
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
"""

import unittest
from typing import List

"""
Approach:
We maintain a running streak of consecutive zeros. 
For each zero encountered, we increment the streak 
and add it to the result, because each new zero extends 
all existing zero subarrays by 1 and also starts a new subarray. 
This avoids recomputation and gives an O(n) solution.
"""

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        result = streak = 0
        for num in nums:
            if num == 0:
                streak += 1
                result += streak
            else:
                streak = 0
        return result


class TestZeroFilledSubarray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [1, 3, 0, 0, 2, 0, 0, 4]
        self.assertEqual(self.solution.zeroFilledSubarray(nums), 6)

    def test_example_2(self):
        nums = [0, 0, 0, 2, 0, 0]
        self.assertEqual(self.solution.zeroFilledSubarray(nums), 9)

    def test_example_3(self):
        nums = [2, 10, 2019]
        self.assertEqual(self.solution.zeroFilledSubarray(nums), 0)

    def test_single_zero(self):
        nums = [0]
        self.assertEqual(self.solution.zeroFilledSubarray(nums), 1)

    def test_three_zeros(self):
        nums = [0, 0, 0]
        self.assertEqual(self.solution.zeroFilledSubarray(nums), 6)

    def test_alternating(self):
        nums = [1, 0, 1, 0, 1, 0]
        self.assertEqual(self.solution.zeroFilledSubarray(nums), 3)


if __name__ == "__main__":
    unittest.main()

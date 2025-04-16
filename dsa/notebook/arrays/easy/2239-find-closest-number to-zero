"""
2239. Find Closest Number to Zero

Given an integer array `nums` of size n, return the number with the value closest to 0 in `nums`. 

If there are multiple answers, return the number with the largest value.

Example 1:
Input: nums = [-4,-2,1,4,8]
Output: 1

Example 2:
Input: nums = [2,-1,1]
Output: 1

Constraints:
- 1 <= nums.length <= 1000
- -10⁵ <= nums[i] <= 10⁵
"""

from typing import List
import unittest

"""
Approach:

- find abs value, and assign to closest
- check if abs(num) and abs(prev closest), update closest to max(num, closest)

"""

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = float("inf")
        for num in nums:
            if abs(num) < abs(closest):
                closest = num
            elif abs(num) == abs(closest):
                closest = max(closest, num)
        return closest


class TestFindClosestNumber(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.findClosestNumber([-4, -2, 1, 4, 8]), 1)

    def test_example_2(self):
        self.assertEqual(self.solution.findClosestNumber([2, -1, 1]), 1)

    def test_single_element(self):
        self.assertEqual(self.solution.findClosestNumber([0]), 0)

    def test_negative_and_positive_equal(self):
        self.assertEqual(self.solution.findClosestNumber([-2, 2]), 2)

    def test_all_negatives(self):
        self.assertEqual(self.solution.findClosestNumber([-9, -7, -2, -1]), -1)

if __name__ == "__main__":
    unittest.main()

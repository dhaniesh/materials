"""
Title: Two Sum II - Input Array Is Sorted

Problem Statement:
Given a 1-indexed array of integers `numbers` that is already sorted in non-decreasing order, 
find two numbers such that they add up to a specific `target` number. Return the indices of 
the two numbers (1-indexed) as an integer array `[index1, index2]` where `index1 < index2`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Your solution must use only constant extra space.

Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2.

Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]

Example 3:
Input: numbers = [-1,0], target = -1
Output: [1,2]

Approach:
Use the two-pointer technique:
1. Initialize left (`l`) at 0 and right (`r`) at the last index.
2. While `l < r`, compute the sum:
   - If sum equals target → return [l+1, r+1]
   - If sum > target → move `r` left
   - Else → move `l` right
This approach works in O(n) time and O(1) space.
"""

from typing import List
import unittest

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        while l < r:
            sums = nums[l] + nums[r]
            if sums == target:
                return [l + 1, r + 1]
            elif sums > target:
                r -= 1
            else:
                l += 1


class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [2, 7, 11, 15]
        target = 9
        expected = [1, 2]
        self.assertEqual(self.solution.twoSum(nums, target), expected)

    def test_example_2(self):
        nums = [2, 3, 4]
        target = 6
        expected = [1, 3]
        self.assertEqual(self.solution.twoSum(nums, target), expected)

    def test_example_3(self):
        nums = [-1, 0]
        target = -1
        expected = [1, 2]
        self.assertEqual(self.solution.twoSum(nums, target), expected)

    def test_large_input(self):
        nums = [1, 2, 3, 4, 4, 9, 56, 90]
        target = 8
        expected = [4, 5]
        self.assertEqual(self.solution.twoSum(nums, target), expected)

    def test_negative_numbers(self):
        nums = [-10, -5, 0, 3, 8, 12]
        target = 3
        expected = [2, 5]
        self.assertEqual(self.solution.twoSum(nums, target), expected)


if __name__ == "__main__":
    unittest.main()

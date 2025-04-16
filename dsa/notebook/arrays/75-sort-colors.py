"""
75. Sort Colors

Given an array `nums` with `n` objects colored red, white, or blue, 
sort them in-place so that objects of the same color are adjacent, 
with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem **without using the library's sort function**.

Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]

Constraints:
- n == nums.length
- 1 <= n <= 300
- nums[i] is either 0, 1, or 2

Follow up: Could you come up with a one-pass algorithm using only constant extra space?
"""

from typing import List
import unittest

"""
Approach:


"""


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        left = i = 0
        right = len(nums)-1

        while i <= right:
            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                i += 1
                left += 1
            elif nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
            else:  # it's a 1
                i += 1
        


class TestSortColors(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [2, 0, 2, 1, 1, 0]
        self.solution.sortColors(nums)
        self.assertEqual(nums, [0, 0, 1, 1, 2, 2])

    def test_example_2(self):
        nums = [2, 0, 1]
        self.solution.sortColors(nums)
        self.assertEqual(nums, [0, 1, 2])

    def test_all_same(self):
        nums = [1, 1, 1]
        self.solution.sortColors(nums)
        self.assertEqual(nums, [1, 1, 1])

    def test_sorted_input(self):
        nums = [0, 1, 2]
        self.solution.sortColors(nums)
        self.assertEqual(nums, [0, 1, 2])

    def test_reverse_sorted(self):
        nums = [2, 1, 0]
        self.solution.sortColors(nums)
        self.assertEqual(nums, [0, 1, 2])


if __name__ == "__main__":
    unittest.main()

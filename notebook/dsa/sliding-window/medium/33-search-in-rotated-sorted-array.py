"""
33. Search in Rotated Sorted Array (Medium)

You are given an integer array nums sorted in ascending order, and an integer target.

Suppose that nums is rotated at some pivot index k (0 <= k < nums.length) such that the resulting 
array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], ..., nums[k-1]] (0-indexed). 

Return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1

Constraints:
- 1 <= nums.length <= 5000
- -10⁴ <= nums[i] <= 10⁴
- All elements of nums are unique.
- nums is guaranteed to be rotated at some pivot.
"""

import unittest

"""
Approach:
We can use binary search to find the target in the rotated sorted array in O(log n) time. 
The key observation is that if the left half is sorted, we can check if the target lies in that range 
and narrow down the search space accordingly.
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pass

class TestSearchInRotatedSortedArray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 0
        self.assertEqual(self.solution.search(nums, target), 4)

    def test_example_2(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 3
        self.assertEqual(self.solution.search(nums, target), -1)

    def test_example_3(self):
        nums = [1]
        target = 0
        self.assertEqual(self.solution.search(nums, target), -1)

    def test_target_not_in_first_half(self):
        nums = [6, 7, 9, 15, 19, 2, 3]
        target = 9
        self.assertEqual(self.solution.search(nums, target), 2)

    def test_target_in_second_half(self):
        nums = [19, 2, 3, 6, 7, 9]
        target = 6
        self.assertEqual(self.solution.search(nums, target), 3)

if __name__ == "__main__":
    unittest.main()

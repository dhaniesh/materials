"""
162. Find Peak Element (Medium)

A peak element in an array is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, 
return the index to any of the peaks.

You must solve it in O(log n) time complexity.

Example 1:
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:
Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index 1 or 5 as both are peak elements.

Constraints:
- 1 <= nums.length <= 2 * 10⁴
- -2³¹ <= nums[i] <= 2³¹ - 1
- nums[i] != nums[i + 1] for all valid i.
"""

import unittest

"""
Approach:
We can use binary search to solve this problem in O(log n) time. The idea is to check the middle element and 
compare it with its neighbors. If it is a peak, return it. Otherwise, if the element on the left is larger, 
the peak must be on the left, and if the element on the right is larger, the peak must be on the right.
"""

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        pass

class TestFindPeakElement(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [1, 2, 3, 1]
        self.assertEqual(self.solution.findPeakElement(nums), 2)

    def test_example_2(self):
        nums = [1, 2, 1, 3, 5, 6, 4]
        self.assertIn(self.solution.findPeakElement(nums), [1, 5])

    def test_single_element(self):
        nums

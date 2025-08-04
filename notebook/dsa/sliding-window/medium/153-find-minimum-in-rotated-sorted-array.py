"""
153. Find Minimum in Rotated Sorted Array (Medium)

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. 
For example, the array nums = [0,1,2,4,5,6,7] might become:
- [4,5,6,7,0,1,2] if it was rotated 4 times.
- [0,1,2,4,5,6,7] if it was rotated 0 times.
Notice that the array may not be sorted.

Given the rotated sorted array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time complexity.

Example 1:
Input: nums = [3,4,5,1,2]
Output: 1

Example 2:
Input: nums = [4,5,6,7,0,1,2]
Output: 0

Example 3:
Input: nums = [11,13,15,17]
Output: 11

Constraints:
- n == nums.length
- 1 <= n <= 5000
- -5000 <= nums[i] <= 5000
- All the integers of nums are unique.
- nums is guaranteed to be rotated at least once.
"""

import unittest

"""
Approach:
We can use binary search to solve this problem in O(log n) time. 
The idea is to compare the middle element with the rightmost element. 
If the middle element is greater than the rightmost element, then the minimum must be in the right half, 
otherwise, it must be in the left half.
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        pass

class TestFindMinimumInRotatedSortedArray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [3, 4, 5, 1, 2]
        self.assertEqual(self.solution.findMin(nums), 1)

    def test_example_2(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        self.assertEqual(self.solution.findMin(nums), 0)

    def test_example_3(self):
        nums = [11, 13, 15, 17]
        self.assertEqual(self.solution.findMin(nums), 11)

    def test_single_element(self):
        nums = [5]
        self.assertEqual(self.solution.findMin(nums), 5)

    def test_no_rotation(self):
        nums = [1, 2, 3, 4, 5]
        self.assertEqual(self.solution.findMin(nums), 1)

if __name__ == "__main__":
    unittest.main()

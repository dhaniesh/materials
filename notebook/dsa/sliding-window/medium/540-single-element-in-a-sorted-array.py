"""
540. Single Element in a Sorted Array (Medium)

You are given a sorted array consisting of only integers where every element appears exactly twice, 
except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.

Example 1:
Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:
Input: nums = [3,3,7,7,10,11,11]
Output: 10

Constraints:
- 1 <= nums.length <= 10⁵
- 0 <= nums[i] <= 10⁶
"""

import unittest

"""
Approach:
We can use binary search to find the single element in O(log n) time. 
The key observation is that in a sorted array where each element except one appears twice, 
the single element will always be at the boundary of a pair. By comparing the middle element 
with its adjacent elements, we can decide which half of the array contains the single element 
and continue the search in that half.
"""

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        pass

class TestSingleElementInSortedArray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
        self.assertEqual(self.solution.singleNonDuplicate(nums), 2)

    def test_example_2(self):
        nums = [3, 3, 7, 7, 10, 11, 11]
        self.assertEqual(self.solution.singleNonDuplicate(nums), 10)

    def test_single_element_at_start(self):
        nums = [1, 1, 2, 2, 3]
        self.assertEqual(self.solution.singleNonDuplicate(nums), 3)

    def test_single_element_at_end(self):
        nums = [0, 2, 2, 3, 3]
        self.assertEqual(self.solution.singleNonDuplicate(nums), 0)

    def test_only_one_element(self):
        nums = [5]
        self.assertEqual(self.solution.singleNonDuplicate(nums), 5)

if __name__ == "__main__":
    unittest.main()

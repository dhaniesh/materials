"""
977. Squares of a Sorted Array (Easy)

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number 
sorted in non-decreasing order.

Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]

Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Constraints:
- 1 <= nums.length <= 10⁴
- -10⁴ <= nums[i] <= 10⁴
- nums is sorted in non-decreasing order.
"""

import unittest

"""
Approach:
We can square each element of the array and then use two pointers (one starting from the beginning and the other from the end) 
to merge the squared elements in sorted order. This approach leverages the fact that the array is already sorted.
"""

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        pass

class TestSquaresOfSortedArray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [-4, -1, 0, 3, 10]
        self.assertEqual(self.solution.sortedSquares(nums), [0, 1, 9, 16, 100])

    def test_example_2(self):
        nums = [-7, -3, 2, 3, 11]
        self.assertEqual(self.solution.sortedSquares(nums), [4, 9, 9, 49, 121])

    def test_single_element(self):
        nums = [5]
        self.assertEqual(self.solution.sortedSquares(nums), [25])

    def test_all_negative(self):
        nums = [-9, -7, -3, -1]
        self.assertEqual(self.solution.sortedSquares(nums), [1, 9, 49, 81])

    def test_all_positive(self):
        nums = [1, 2, 3, 5]
        self.assertEqual(self.solution.sortedSquares(nums), [1, 4, 9, 25])

if __name__ == "__main__":
    unittest.main()

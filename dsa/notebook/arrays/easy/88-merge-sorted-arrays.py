"""
88. Merge Sorted Array

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
representing the number of elements in nums1 and nums2 respectively.

Merge nums2 into nums1 as one sorted array in-place. The final sorted array should not be returned by the function, 
but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, 
where the first m elements denote the elements that should be merged, and the last n elements are set to 0 
and should be ignored. nums2 has a length of n.

Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3  
Output: [1,2,2,3,5,6]

Example 2:
Input: nums1 = [1], m = 1, nums2 = [], n = 0  
Output: [1]

Example 3:
Input: nums1 = [0], m = 0, nums2 = [1], n = 1  
Output: [1]

Constraints:
- nums1.length == m + n
- nums2.length == n
- 0 <= m, n <= 200
- 1 <= m + n <= 200
- -10⁹ <= nums1[i], nums2[i] <= 10⁹

Follow up: Can you come up with an algorithm that runs in O(m + n) time?
"""

from typing import List
import unittest

"""
Approach:

O(m) space
- new array and find the union

O(1) space
- use pointers
"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        m = m-1
        n = n-1
        for i in range(len(nums1)-1, -1, -1):
            if m >=0 and n >= 0 and nums1[m] > nums2[n]:
                nums1[i] = nums1[m]
                m -= 1
            elif n >= 0:
                nums1[i] = nums2[n]
                n -= 1
        

class TestMergeSortedArray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums1 = [1,2,3,0,0,0]
        self.solution.merge(nums1, 3, [2,5,6], 3)
        self.assertEqual(nums1, [1,2,2,3,5,6])

    def test_example_2(self):
        nums1 = [1]
        self.solution.merge(nums1, 1, [], 0)
        self.assertEqual(nums1, [1])

    def test_example_3(self):
        nums1 = [0]
        self.solution.merge(nums1, 0, [1], 1)
        self.assertEqual(nums1, [1])

    def test_custom_case(self):
        nums1 = [4,5,6,0,0,0]
        self.solution.merge(nums1, 3, [1,2,3], 3)
        self.assertEqual(nums1, [1,2,3,4,5,6])

if __name__ == "__main__":
    unittest.main()

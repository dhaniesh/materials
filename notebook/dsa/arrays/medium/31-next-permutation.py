"""
31. Next Permutation

A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

- For example, for arr = [1,2,3], the following are considered permutations: 
  [1,2,3], [1,3,2], [3,1,2], [2,3,1].

The next permutation of an array of integers is the next lexicographically greater permutation of its integer. 
More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, 
then the next permutation of that array is the permutation that follows it in the sorted order.

If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.

Example 1:
Input: nums = [1,2,3]
Output: [1,3,2]

Example 2:
Input: nums = [3,2,1]
Output: [1,2,3]

Example 3:
Input: nums = [1,1,5]
Output: [1,5,1]

Constraints:
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 100
"""

from typing import List
import unittest

"""
Approach:


"""

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        x = -1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                x = i
                break
        
        if x == -1:
            nums[:] = nums[::-1]
            return
        
        y = -1
        for j in range(len(nums)-1, -1, -1):
            if nums[j] > nums[x]:
                y = j
                break
        
        nums[y], nums[x] = nums[x], nums[y]
        nums[x+1:] = nums[x+1:][::-1]
        return

class TestNextPermutation(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [1, 2, 3]
        self.solution.nextPermutation(nums)
        self.assertEqual(nums, [1, 3, 2])

    def test_example_2(self):
        nums = [3, 2, 1]
        self.solution.nextPermutation(nums)
        self.assertEqual(nums, [1, 2, 3])

    def test_example_3(self):
        nums = [1, 1, 5]
        self.solution.nextPermutation(nums)
        self.assertEqual(nums, [1, 5, 1])

    def test_repeat_numbers(self):
        nums = [2, 3, 1, 3, 3]
        self.solution.nextPermutation(nums)
        self.assertEqual(nums, [2, 3, 3, 1, 3])

    def test_single_element(self):
        nums = [1]
        self.solution.nextPermutation(nums)
        self.assertEqual(nums, [1])

if __name__ == "__main__":
    unittest.main()

"""
229. Majority Element II

Given an integer array `nums`, return all the elements that appear more than ⌊ n / 3 ⌋ times in the array.

Example 1:
Input: nums = [3,2,3]
Output: [3]

Example 2:
Input: nums = [1,1,1,3,3,2,2,2]
Output: [1,2]

Constraints:
- 1 <= nums.length <= 5 * 10⁴
- -10^9 <= nums[i] <= 10^9
"""

from typing import List
import unittest

"""
Approach:


"""

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        pass

class TestMajorityElementII(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [3, 2, 3]
        result = self.solution.majorityElement(nums)
        self.assertEqual(result, [3])

    def test_example_2(self):
        nums = [1, 1, 1, 3, 3, 2, 2, 2]
        result = self.solution.majorityElement(nums)
        self.assertEqual(result, [1, 2])

    def test_single_element(self):
        nums = [5]
        result = self.solution.majorityElement(nums)
        self.assertEqual(result, [5])

    def test_all_same(self):
        nums = [3, 3, 3, 3]
        result = self.solution.majorityElement(nums)
        self.assertEqual(result, [3])

    def test_no_majority(self):
        nums = [1, 2, 3, 4, 5, 6]
        result = self.solution.majorityElement(nums)
        self.assertEqual(result, [])

if __name__ == "__main__":
    unittest.main()

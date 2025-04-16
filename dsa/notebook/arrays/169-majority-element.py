"""
169. Majority Element

Given an array `nums` of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

Constraints:
- n == nums.length
- 1 <= n <= 5 * 10⁴
- -10⁹ <= nums[i] <= 10⁹

Follow-up: Could you solve the problem in linear time and in O(1) space?
"""

from typing import List
import unittest

"""
Approach:

Use counter
- counter, most_common

Moore voting algorthm
- use count, majority variables
- if count = 0, majority = num
- if num is same as majority, count ++, else count--
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if count == 0:
                majority = num
            
            if majority == num:
                count += 1
            else:
                count -= 1
        return majority
            

class TestMajorityElement(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.majorityElement([3, 2, 3]), 3)

    def test_example_2(self):
        self.assertEqual(self.solution.majorityElement([2, 2, 1, 1, 1, 2, 2]), 2)

    def test_single_element(self):
        self.assertEqual(self.solution.majorityElement([1]), 1)

    def test_all_same(self):
        self.assertEqual(self.solution.majorityElement([5, 5, 5, 5]), 5)

if __name__ == "__main__":
    unittest.main()

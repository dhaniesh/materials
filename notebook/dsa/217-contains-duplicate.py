"""
217. Contains Duplicate

Given an integer array nums, return true if any value appears at least twice 
in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: True
Explanation: The element 1 occurs twice.

Example 2:
Input: nums = [1,2,3,4]
Output: False
Explanation: All elements are distinct.

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: True
Explanation: Multiple duplicates exist.

Approach:
- Use a hash map (dictionary) to track seen numbers.
- Return True when a duplicate is found; otherwise, False.
"""

import unittest

class Solution(object):
    def containsDuplicate(self, nums):
        hash_nums = {}
        for num in nums:
            if num in hash_nums:
                return True
            hash_nums[num] = 1
        return False


class TestContainsDuplicate(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_has_duplicate(self):
        self.assertTrue(self.sol.containsDuplicate([1, 2, 3, 1]))

    def test_no_duplicate(self):
        self.assertFalse(self.sol.containsDuplicate([1, 2, 3, 4]))

    def test_large_with_duplicates(self):
        self.assertTrue(self.sol.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))

    def test_empty_list(self):
        self.assertFalse(self.sol.containsDuplicate([]))

    def test_single_element(self):
        self.assertFalse(self.sol.containsDuplicate([99]))

    def test_negative_numbers(self):
        self.assertTrue(self.sol.containsDuplicate([-1, -2, -3, -1]))

    def test_large_unique(self):
        nums = list(range(10000))
        self.assertFalse(self.sol.containsDuplicate(nums))


if __name__ == "__main__":
    unittest.main()

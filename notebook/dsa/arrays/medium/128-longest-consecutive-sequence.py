"""
128. Longest Consecutive Sequence

Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Constraints:
- 0 <= nums.length <= 10⁵
- -10⁹ <= nums[i] <= 10⁹
"""

from typing import List
import unittest

"""
Approach:
- use set to remove duplicates
- check if num-1 exists, if so skip
- else calculate length

"""


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        nums_set = set(nums)
        for num in nums_set:
            length = 1
            if num-1 not in nums_set:
                while num+1 in nums_set:
                    length += 1
                    num = num+1
                result = max(result, length)
        return result


class TestLongestConsecutiveSequence(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.longestConsecutive(
            [100, 4, 200, 1, 3, 2]), 4)

    def test_example_2(self):
        self.assertEqual(self.solution.longestConsecutive(
            [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]), 9)

    def test_single_element(self):
        self.assertEqual(self.solution.longestConsecutive([5]), 1)

    def test_empty(self):
        self.assertEqual(self.solution.longestConsecutive([]), 0)

    def test_duplicates(self):
        self.assertEqual(self.solution.longestConsecutive([1, 2, 2, 3]), 3)

    def test_negative_numbers(self):
        self.assertEqual(
            self.solution.longestConsecutive([-2, -3, -1, 0, 1]), 5)


if __name__ == "__main__":
    unittest.main()

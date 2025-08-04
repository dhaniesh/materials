"""
228. Summary Ranges

You are given a sorted unique integer array `nums`. Return the smallest sorted list of ranges that cover all the numbers in the array exactly. 
That is, each of the ranges [start, end] should be such that start <= end and that each number in `nums` is covered by at least one of the ranges.

Example 1:
Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]

Example 2:
Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]

Constraints:
- 0 <= nums.length <= 20
- -2³¹ <= nums[i] <= 2³¹ - 1
- nums consists of unique values sorted in ascending order.
"""

from typing import List
import unittest

"""
Approach:


"""


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        ranges = []
        i = j = 0
        while i <= j < len(nums):
            if nums[j] != nums[-1] and nums[j]+1 == nums[j+1]:
                j += 1
            else:
                ranges.append([nums[i], nums[j]])
                j += 1
                i = j

        for _rnge in ranges:
            if _rnge[0] == _rnge[-1]:
                result.append(f'{_rnge[0]}')
            else:
                result.append(f'{_rnge[0]}->{_rnge[-1]}')
        return result


class TestSummaryRanges(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [0, 1, 2, 4, 5, 7]
        result = self.solution.summaryRanges(nums)
        self.assertEqual(result, ["0->2", "4->5", "7"])

    def test_example_2(self):
        nums = [0, 2, 3, 4, 6, 8, 9]
        result = self.solution.summaryRanges(nums)
        self.assertEqual(result, ["0", "2->4", "6", "8->9"])

    def test_single_element(self):
        nums = [1]
        result = self.solution.summaryRanges(nums)
        self.assertEqual(result, ["1"])

    def test_empty(self):
        nums = []
        result = self.solution.summaryRanges(nums)
        self.assertEqual(result, [])

    def test_no_consecutive(self):
        nums = [1, 3, 5, 7]
        result = self.solution.summaryRanges(nums)
        self.assertEqual(result, ["1", "3", "5", "7"])


if __name__ == "__main__":
    unittest.main()

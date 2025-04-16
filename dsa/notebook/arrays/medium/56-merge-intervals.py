"""
56. Merge Intervals

Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]

Constraints:
- 1 <= intervals.length <= 10⁴
- intervals[i].length == 2
- 0 <= start_i <= end_i <= 10⁴
"""

from typing import List
import unittest

"""
Approach:


"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        pass

class TestMergeIntervals(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        intervals = [[1,3],[2,6],[8,10],[15,18]]
        result = self.solution.merge(intervals)
        self.assertEqual(result, [[1,6],[8,10],[15,18]])

    def test_example_2(self):
        intervals = [[1,4],[4,5]]
        result = self.solution.merge(intervals)
        self.assertEqual(result, [[1,5]])

    def test_no_overlap(self):
        intervals = [[1,2],[3,4],[5,6]]
        result = self.solution.merge(intervals)
        self.assertEqual(result, [[1,2],[3,4],[5,6]])

    def test_full_overlap(self):
        intervals = [[1,10],[2,3],[4,5]]
        result = self.solution.merge(intervals)
        self.assertEqual(result, [[1,10]])

    def test_nested_and_adjacent(self):
        intervals = [[1,4],[0,2],[3,5]]
        result = self.solution.merge(intervals)
        self.assertEqual(result, [[0,5]])

if __name__ == "__main__":
    unittest.main()

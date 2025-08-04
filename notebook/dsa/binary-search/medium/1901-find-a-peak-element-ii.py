"""
1901. Find a Peak Element II (Medium)

A peak element in a 2D grid is an element that is strictly greater than all of its adjacent neighbors to the left, right, top, and bottom.

Given a 0-indexed `m x n` matrix `mat` where no two adjacent cells are equal, find any peak element `mat[i][j]` and return the length 2 array `[i, j]`.

You may assume that the entire matrix is surrounded by an outer perimeter with the value -1 in each cell. You must write an algorithm that runs in O(m log n) or O(n log m) time.

Example 1:
Input: mat = [[1,4],[3,2]]
Output: [0,1]

Example 2:
Input: mat = [[10,20,15],[21,30,14],[7,16,32]]
Output: [1,1]

Constraints:
- m == mat.length
- n == mat[i].length
- 1 <= m, n <= 500
- 1 <= mat[i][j] <= 10⁵
- No two adjacent cells are equal.
"""

from typing import List
import unittest

"""
Approach:


"""

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        pass

class TestFindPeakElementII(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        mat = [[1, 4], [3, 2]]
        result = self.solution.findPeakGrid(mat)
        self.assertIn(result, [[0, 1], [1, 0]])  # depending on which valid peak is found

    def test_example_2(self):
        mat = [[10, 20, 15], [21, 30, 14], [7, 16, 32]]
        result = self.solution.findPeakGrid(mat)
        self.assertIn(result, [[1, 1], [2, 2]])  # either valid peak position is acceptable

    def test_single_row(self):
        mat = [[1, 3, 2]]
        result = self.solution.findPeakGrid(mat)
        self.assertIn(result, [[0, 1]])

    def test_single_column(self):
        mat = [[1], [4], [2]]
        result = self.solution.findPeakGrid(mat)
        self.assertIn(result, [[1, 0]])

    def test_peak_in_corner(self):
        mat = [[9, 1], [2, 3]]
        result = self.solution.findPeakGrid(mat)
        self.assertIn(result, [[0, 0]])

if __name__ == "__main__":
    unittest.main()

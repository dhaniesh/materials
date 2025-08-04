"""
73. Set Matrix Zeroes

Given an `m x n` integer matrix `matrix`, if an element is 0, set its entire row and column to 0's.

You must do it in place.

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

Constraints:
- m == matrix.length
- n == matrix[0].length
- 1 <= m, n <= 200
- -2³¹ <= matrix[i][j] <= 2³¹ - 1

Follow up:
- A straightforward solution using O(m * n) space is probably a bad idea.
- A simple improvement uses O(m + n) space, but still not the best solution.
- Could you devise a constant space solution?
"""

from typing import List
import unittest

"""
Approach:
- use set to track zeros

"""

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        col_0 = 1
        row, col = len(matrix), len(matrix[0])
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    if j == 0:
                        col_0 = 0
                    else:
                        matrix[0][j] = 0
        
        for i in range(1, row):
            for j in range(1, col):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        
        if matrix[0][0] == 0:
            for j in range(col):
                matrix[0][j] = 0
        if col_0 == 0:
            for i in range(row):
                matrix[i][0] = 0
        return

class TestSetMatrixZeroes(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        matrix = [[1,1,1],[1,0,1],[1,1,1]]
        self.solution.setZeroes(matrix)
        self.assertEqual(matrix, [[1,0,1],[0,0,0],[1,0,1]])

    def test_example_2(self):
        matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
        self.solution.setZeroes(matrix)
        self.assertEqual(matrix, [[0,0,0,0],[0,4,5,0],[0,3,1,0]])

    def test_no_zero(self):
        matrix = [[1,2],[3,4]]
        self.solution.setZeroes(matrix)
        self.assertEqual(matrix, [[1,2],[3,4]])

    def test_all_zeros(self):
        matrix = [[0,0],[0,0]]
        self.solution.setZeroes(matrix)
        self.assertEqual(matrix, [[0,0],[0,0]])

    def test_single_row(self):
        matrix = [[1,0,3]]
        self.solution.setZeroes(matrix)
        self.assertEqual(matrix, [[0,0,0]])

    def test_single_column(self):
        matrix = [[1],[0],[3]]
        self.solution.setZeroes(matrix)
        self.assertEqual(matrix, [[0],[0],[0]])

if __name__ == "__main__":
    unittest.main()

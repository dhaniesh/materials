"""
74. Search a 2D Matrix (Medium)

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
- Integers in each row are sorted from left to right.
- The first integer of each row is greater than the last integer of the previous row.

Example 1:
Input: matrix = [
  [1,   4,  7, 11],
  [2,   5,  8, 12],
  [3,   6,  9, 16],
  [10, 11, 13, 17]
], target = 5
Output: true

Example 2:
Input: matrix = [
  [1,   4,  7, 11],
  [2,   5,  8, 12],
  [3,   6,  9, 16],
  [10, 11, 13, 17]
], target = 20
Output: false

Constraints:
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 100
- -10⁴ <= matrix[i][j] <= 10⁴
- -10⁴ <= target <= 10⁴
"""

from typing import List
import unittest

"""
Approach:
The matrix has sorted rows and columns, which means we can use a binary search-like approach.
We can start from the top-right or bottom-left and reduce the search space based on the comparison with the target.
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bot = len(matrix) - 1
        while top <= bot:
            mid = (top + bot) // 2
            if matrix[mid][0] < target and matrix[mid][-1] > target:
                break
            elif matrix[mid][0] > target:
                bot = mid - 1
            else:
                top = mid + 1
        row = (top + bot) // 2

        left = 0
        right = len(matrix[row]) - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                right = mid - 1
            else:
                left = mid + 1 
        return False


class TestSearch2DMatrix(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        matrix = [
            [1, 4, 7, 11],
            [2, 5, 8, 12],
            [3, 6, 9, 16],
            [10, 11, 13, 17]
        ]
        target = 5
        self.assertTrue(self.solution.searchMatrix(matrix, target))

    def test_example_2(self):
        matrix = [
            [1, 4, 7, 11],
            [2, 5, 8, 12],
            [3, 6, 9, 16],
            [10, 11, 13, 17]
        ]
        target = 20
        self.assertFalse(self.solution.searchMatrix(matrix, target))

    def test_single_row_matrix(self):
        matrix = [
            [1, 2, 3, 4]
        ]
        target = 3
        self.assertTrue(self.solution.searchMatrix(matrix, target))

    def test_single_column_matrix(self):
        matrix = [
            [1],
            [2],
            [3],
            [4]
        ]
        target = 2
        self.assertTrue(self.solution.searchMatrix(matrix, target))

if __name__ == "__main__":
    unittest.main()

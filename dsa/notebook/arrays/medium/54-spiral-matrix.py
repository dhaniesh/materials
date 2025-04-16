"""
54. Spiral Matrix

Given an `m x n` matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 10
- -100 <= matrix[i][j] <= 100
"""

from typing import List
import unittest

"""
Approach:


"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        pass

class TestSpiralMatrix(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        matrix = [[1,2,3],[4,5,6],[7,8,9]]
        result = self.solution.spiralOrder(matrix)
        self.assertEqual(result, [1,2,3,6,9,8,7,4,5])

    def test_example_2(self):
        matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
        result = self.solution.spiralOrder(matrix)
        self.assertEqual(result, [1,2,3,4,8,12,11,10,9,5,6,7])

    def test_single_element(self):
        matrix = [[5]]
        result = self.solution.spiralOrder(matrix)
        self.assertEqual(result, [5])

    def test_single_row(self):
        matrix = [[1,2,3,4]]
        result = self.solution.spiralOrder(matrix)
        self.assertEqual(result, [1,2,3,4])

    def test_single_column(self):
        matrix = [[1],[2],[3]]
        result = self.solution.spiralOrder(matrix)
        self.assertEqual(result, [1,2,3])

if __name__ == "__main__":
    unittest.main()

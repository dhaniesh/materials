"""
36. Valid Sudoku (Medium)

Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the rules:
- Each row must contain the digits 1-9 without repetition.
- Each column must contain the digits 1-9 without repetition.
- Each of the nine 3x3 sub-boxes must contain the digits 1-9 without repetition.

Example 1:
Input: board = 
[["5","3",".",".","7",".",".",".","."]
 ["6",".",".","1","9","5",".",".","."]
 [".","9","8",".",".",".",".","6","."]
 ["8",".",".",".","6",".",".",".","3"]
 ["4",".",".","8",".","3",".",".","1"]
 ["7",".",".",".","2",".",".",".","6"]
 [".","6",".",".",".",".","2","8","."]
 [".",".",".","4","1","9",".",".","5"]
 [".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:
Input: board = 
[["8","3",".",".","7",".",".",".","."]
 ["6",".",".","1","9","5",".",".","."]
 [".","9","8",".",".",".",".","6","."]
 ["8",".",".",".","6",".",".",".","3"]
 ["4",".",".","8",".","3",".",".","1"]
 ["7",".",".",".","2",".",".",".","6"]
 [".","6",".",".",".",".","2","8","."]
 [".",".",".","4","1","9",".",".","5"]
 [".",".",".",".","8",".",".","7","9"]]
Output: false
"""

import unittest

"""
Approach:
We can use sets to track seen numbers for each row, column, and 3x3 box.
Iterate through each cell, and validate no duplicates are seen.
"""

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        pass

class TestValidSudoku(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_valid_board(self):
        board = [
            ["5","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
        ]
        self.assertTrue(self.solution.isValidSudoku(board))

    def test_invalid_board(self):
        board = [
            ["8","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
        ]
        self.assertFalse(self.solution.isValidSudoku(board))

if __name__ == "__main__":
    unittest.main()

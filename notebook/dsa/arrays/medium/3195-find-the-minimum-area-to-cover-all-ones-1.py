"""
You are given a 2D binary array grid. Find a rectangle with horizontal and vertical sides with the smallest area, such that all the 1's in grid lie inside this rectangle.
Return the minimum possible area of the rectangle.

Example 1:
Input: grid = [[0,1,0],[1,0,1]]
Output: 6
Explanation: The smallest rectangle has a height of 2 and a width of 3, so it has an area of 2 * 3 = 6.

Example 2:
Input: grid = [[1,0],[0,0]]
Output: 1
Explanation: The smallest rectangle has both height and width 1, so its area is 1 * 1 = 1.

Constraints:
- 1 <= grid.length, grid[i].length <= 1000
- grid[i][j] is either 0 or 1.
- The input is generated such that there is at least one 1 in grid.

"""
from typing import List
import unittest

class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        top = bottom = left = right = None

        # find top
        for i in range(n):
            if 1 in grid[i]:
                top = i
                break
        
        # find bottom
        for i in reversed(range(n)):
            if 1 in grid[i]:
                bottom = i
                break

        # find left
        for j in range(m):
            if any(grid[i][j] == 1 for i in range(n)):
                left = j
                break

        # find right
        for j in reversed(range(m)):
            if any(grid[i][j] == 1 for i in range(n)):
                right = j
                break

        return (bottom - top + 1) * (right - left + 1)


class TestFindMinimumArea(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    # 1. Single cell with 1
    def test_single_cell_one(self):
        grid = [[1]]
        self.assertEqual(self.solution.minimumArea(grid), 1)

    # 3. Small square cluster
    def test_small_square(self):
        grid = [
            [0, 0],
            [0, 1]
        ]
        self.assertEqual(self.solution.minimumArea(grid), 1)

    # 4. Rectangle cluster of ones
    def test_rectangle_one_cluster(self):
        grid = [
            [0, 0, 0, 0],
            [0, 1, 1, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0]
        ]
        self.assertEqual(self.solution.minimumArea(grid), 4)

    # 5. Sparse grid
    def test_sparse_grid(self):
        grid = [
            [0, 0, 0, 1],
            [0, 0, 0, 0],
            [0, 0, 1, 0],
        ]
        # top=0, bottom=2, left=2, right=3 => area = 3*2=6
        self.assertEqual(self.solution.minimumArea(grid), 6)
    

if __name__ == "__main__":
    unittest.main()

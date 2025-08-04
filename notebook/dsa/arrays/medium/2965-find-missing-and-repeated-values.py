"""
2965. Find Missing and Repeated Values

You are given a 0-indexed 2D integer array `grid` of size 3 x 3, representing a 3 x 3 grid containing integers from 1 to 9, 
except that one number is missing and another number is repeated.

Return an array `ans` of size 2 where:
- `ans[0]` is the repeated number, and
- `ans[1]` is the missing number.

Example 1:
Input: grid = [[8,3,4],[1,5,9],[6,7,3]]
Output: [3,2]
Explanation: 3 is repeated and 2 is missing, so we return [3,2].

Example 2:
Input: grid = [[4,2,7],[3,1,8],[6,5,9]]
Output: [0,0]
Explanation: No number is missing or repeated, so we return [0,0].

Constraints:
- grid.length == 3
- grid[i].length == 3
- 0 <= grid[i][j] <= 9
"""

from typing import List
import unittest

"""
Approach:
- use array and it's indexes instead of a hashmap
- why? range is always within 1 and 9

"""

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        occurence = [0] * (n*n + 1)
        for i in range(len(grid)):
            for j in range(len(grid)):
                if occurence[grid[i][j]]:
                    duplicate = grid[i][j]
                occurence[grid[i][j]] +=1

        for i, count in enumerate(occurence):
            if i and count == 0:
                return [duplicate, i]          
        return [0, 0]  

class TestFindMissingAndRepeatedValues(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        grid = [[8,3,4],[1,5,9],[6,7,3]]
        result = self.solution.findMissingAndRepeatedValues(grid)
        self.assertEqual(result, [3,2])

    def test_example_2(self):
        grid = [[4,2,7],[3,1,8],[6,5,9]]
        result = self.solution.findMissingAndRepeatedValues(grid)
        self.assertEqual(result, [0,0])

    def test_missing_1(self):
        grid = [[2,3,4],[5,6,7],[8,9,2]]
        result = self.solution.findMissingAndRepeatedValues(grid)
        self.assertEqual(result, [2,1])

    def test_missing_9(self):
        grid = [[1,2,3],[4,5,6],[7,8,8]]
        result = self.solution.findMissingAndRepeatedValues(grid)
        self.assertEqual(result, [8,9])

if __name__ == "__main__":
    unittest.main()

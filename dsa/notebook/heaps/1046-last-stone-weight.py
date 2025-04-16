"""
1046. Last Stone Weight (Easy)

We have a collection of stones, where each stone has a positive integer weight. 
Each turn, we choose the two heaviest stones and smash them together. 
The result of this smash is:
- If both stones have the same weight, both stones are destroyed.
- If the stones have different weights, the smaller stone is destroyed and the larger stone's weight is reduced by the weight of the smaller stone.

Return the weight of the last remaining stone. If there are no stones left, return 0.
"""

import unittest

"""
Approach:


"""

class Solution:
    def lastStoneWeight(self, stones):
        pass

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example(self):
        self.assertEqual(self.solution.lastStoneWeight([2, 7, 4, 1, 8, 1]), 1)

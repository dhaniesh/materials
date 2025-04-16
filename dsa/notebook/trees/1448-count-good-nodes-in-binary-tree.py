"""
1448. Count Good Nodes in Binary Tree (Medium)

A node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.
Return the number of good nodes.
"""

import unittest

"""
Approach:


"""

class Solution:
    def goodNodes(self, root):
        pass

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example(self):
        self.assertEqual(self.solution.goodNodes(None), 0)

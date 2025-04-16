"""
105. Construct Binary Tree from Preorder and Inorder Traversal (Medium)

Build a binary tree from its preorder and inorder traversal.
"""

import unittest

"""
Approach:


"""

class Solution:
    def buildTree(self, preorder, inorder):
        pass

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example(self):
        self.assertIsNone(self.solution.buildTree([], []))

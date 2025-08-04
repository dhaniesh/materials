"""
543. Diameter of Binary Tree (Easy)

Given the root of a binary tree, return the length of the diameter of the tree.

Example:
Input: [1,2,3,4,5]
Output: 3
"""

import unittest

"""
Approach:
Use DFS to compute the longest path between any two nodes in the tree.
"""

class Solution:
    def diameterOfBinaryTree(self, root):
        pass

class TestDiameterOfBinaryTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example(self):
        self.assertEqual(self.solution.diameterOfBinaryTree(None), 0)  # Placeholder

if __name__ == "__main__":
    unittest.main()

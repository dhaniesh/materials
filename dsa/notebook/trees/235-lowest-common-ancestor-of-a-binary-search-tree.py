"""
235. Lowest Common Ancestor of a Binary Search Tree (Medium)

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
"""

import unittest

"""
Approach:
Use the properties of a BST to move left or right based on values.
"""

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        pass

class TestLowestCommonAncestor(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic(self):
        self.assertIsNone(self.solution.lowestCommonAncestor(None, None, None))  # Placeholder

if __name__ == "__main__":
    unittest.main()

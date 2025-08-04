"""
110. Balanced Binary Tree (Easy)

Check if a binary tree is height-balanced.

Example:
Input: [3,9,20,null,null,15,7]
Output: true
"""

import unittest

"""
Approach:
Use post-order DFS to check height balance at every node.
"""

class Solution:
    def isBalanced(self, root):
        pass

class TestBalancedBinaryTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example(self):
        self.assertTrue(self.solution.isBalanced(None))  # Placeholder

if __name__ == "__main__":
    unittest.main()

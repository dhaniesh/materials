"""
226. Invert Binary Tree (Easy)

Invert a binary tree.

Example:
Input: [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
"""

import unittest

"""
Approach:
We can use recursion or BFS to swap the left and right children of each node.
"""

class Solution:
    def invertTree(self, root):
        pass

class TestInvertBinaryTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example(self):
        # Input and output should be TreeNode structures. Assume helper functions are available for conversion if needed.
        self.assertIsNotNone(self.solution.invertTree(None))  # Placeholder

if __name__ == "__main__":
    unittest.main()

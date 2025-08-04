"""
104. Maximum Depth of Binary Tree (Easy)

Given a binary tree, find its maximum depth.

Example:
Input: [3,9,20,null,null,15,7]
Output: 3
"""

import unittest

"""
Approach:
Use DFS to traverse down each path and find the maximum depth.
"""

class Solution:
    def maxDepth(self, root):
        pass

class TestMaxDepth(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example(self):
        self.assertEqual(self.solution.maxDepth(None), 0)  # Placeholder

if __name__ == "__main__":
    unittest.main()

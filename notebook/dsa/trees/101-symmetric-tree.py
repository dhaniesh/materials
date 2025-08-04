"""
101. Symmetric Tree (Easy)

Check whether a binary tree is a mirror of itself.

Example:
Input: [1,2,2,3,4,4,3]
Output: true
"""

import unittest

"""
Approach:
Use recursion to check if left and right subtrees are mirrors.
"""

class Solution:
    def isSymmetric(self, root):
        pass

class TestSymmetricTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example(self):
        self.assertTrue(self.solution.isSymmetric(None))  # Placeholder

if __name__ == "__main__":
    unittest.main()

"""
100. Same Tree (Easy)

Check if two binary trees are the same.

Example:
Input: p = [1,2,3], q = [1,2,3]
Output: true
"""

import unittest

"""
Approach:
Use recursion to compare values and structure node-by-node.
"""

class Solution:
    def isSameTree(self, p, q):
        pass

class TestSameTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example(self):
        self.assertTrue(self.solution.isSameTree(None, None))  # Placeholder

if __name__ == "__main__":
    unittest.main()

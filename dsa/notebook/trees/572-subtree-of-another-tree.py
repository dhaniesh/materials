"""
572. Subtree of Another Tree (Easy)

Check if one tree is a subtree of another.

Example:
Input: s = [3,4,5,1,2], t = [4,1,2]
Output: true
"""

import unittest

"""
Approach:
Traverse the main tree and check for same structure using isSameTree function.
"""

class Solution:
    def isSubtree(self, s, t):
        pass

class TestSubtreeOfAnotherTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example(self):
        self.assertTrue(self.solution.isSubtree(None, None))  # Placeholder

if __name__ == "__main__":
    unittest.main()

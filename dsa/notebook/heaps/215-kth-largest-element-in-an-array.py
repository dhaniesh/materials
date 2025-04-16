"""
215. Kth Largest Element in an Array (Medium)

Find the kth largest element in an unsorted array.
"""

import unittest

"""
Approach:


"""

class Solution:
    def findKthLargest(self, nums, k):
        pass

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example(self):
        self.assertEqual(self.solution.findKthLargest([3,2,1,5,6,4], 2), 5)

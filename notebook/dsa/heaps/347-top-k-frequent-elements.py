"""
347. Top K Frequent Elements (Medium)

Given a non-empty array of integers, return the k most frequent elements.
"""

import unittest

"""
Approach:


"""

from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        pass

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example(self):
        self.assertEqual(self.solution.topKFrequent([1,1,1,2,2,3], 2), [1, 2])

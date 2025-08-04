"""
973. K Closest Points to Origin (Medium)

Given an array of points in the 2D plane, find the k closest points to the origin (0, 0).
"""

import unittest

"""
Approach:


"""

import heapq

class Solution:
    def kClosest(self, points, k):
        pass

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example(self):
        self.assertEqual(self.solution.kClosest([[1,3],[-2,2]], 1), [[-2, 2]])

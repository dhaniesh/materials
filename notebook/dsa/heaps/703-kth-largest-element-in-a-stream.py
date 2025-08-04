"""
703. Kth Largest Element in a Stream (Easy)

Design a class to find the kth largest element in a stream. 
Implement the KthLargest class that takes an integer k and a list of integers nums. 
It should have a method `add(val)` that adds a new integer to the stream and returns the kth largest element.
"""

import unittest

"""
Approach:


"""

import heapq

class KthLargest:

    def __init__(self, k, nums):
        pass

    def add(self, val):
        pass


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.kthLargest = KthLargest(3, [4, 5, 8, 2])

    def test_example(self):
        self.assertEqual(self.kthLargest.add(3), 4)
        self.assertEqual(self.kthLargest.add(5), 5)
        self.assertEqual(self.kthLargest.add(10), 5)
        self.assertEqual(self.kthLargest.add(9), 8)

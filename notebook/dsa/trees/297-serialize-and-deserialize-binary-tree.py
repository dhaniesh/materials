"""
297. Serialize and Deserialize Binary Tree (Hard)

Design an algorithm to serialize and deserialize a binary tree.
"""

import unittest

"""
Approach:


"""

class Codec:
    def serialize(self, root):
        pass

    def deserialize(self, data):
        pass

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.codec = Codec()

    def test_example(self):
        self.assertIsNone(self.codec.deserialize(self.codec.serialize(None)))

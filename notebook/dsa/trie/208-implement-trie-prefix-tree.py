"""
208. Implement Trie (Prefix Tree) (Medium)

Implement a trie with insert, search, and startsWith methods.
"""

import unittest

"""
Approach:


"""

class Trie:

    def __init__(self):
        pass

    def insert(self, word: str) -> None:
        pass

    def search(self, word: str) -> bool:
        pass

    def startsWith(self, prefix: str) -> bool:
        pass


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()

    def test_example(self):
        self.trie.insert("apple")
        self.assertTrue(self.trie.search("apple"))
        self.assertFalse(self.trie.search("app"))
        self.assertTrue(self.trie.startsWith("app"))

"""
211. Design Add and Search Words Data Structure (Medium)

Design a data structure that supports the following methods: addWord, search, and startsWith.
"""

import unittest

"""
Approach:


"""

class WordDictionary:

    def __init__(self):
        pass

    def addWord(self, word: str) -> None:
        pass

    def search(self, word: str) -> bool:
        pass


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.word_dict = WordDictionary()

    def test_example(self):
        self.word_dict.addWord("bad")
        self.assertTrue(self.word_dict.search("bad"))
        self.assertFalse(self.word_dict.search("b.d"))

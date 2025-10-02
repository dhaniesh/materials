"""
2942. Find Words Containing Character

You are given a 0-indexed array of strings words and a character x.
Return an array of indices representing the words that contain the character x.
Note that the returned array may be in any order.

Example 1:
Input: words = ["leet","code"], x = "e"
Output: [0,1]
Explanation: "e" occurs in both words: "leet", and "code". Hence, we return indices 0 and 1.

Example 2:
Input: words = ["abc","bcd","aaaa","cbc"], x = "a"
Output: [0,2]
Explanation: "a" occurs in "abc", and "aaaa". Hence, we return indices 0 and 2.

Example 3:
Input: words = ["abc","bcd","aaaa","cbc"], x = "z"
Output: []
Explanation: "z" does not occur in any of the words. Hence, we return an empty array.

Approach:
- Iterate and check, append index when true
"""

import unittest
from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = []
        for i, word in enumerate(words):
            if x in word:
                res.append(i)
        return res

class TestFindWordsContaining(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_basic(self):
        self.assertEqual(self.sol.findWordsContaining(["apple", "banana", "cherry", "date"], "a"), [0, 1, 3])

    def test_not_found(self):
        self.assertEqual(self.sol.findWordsContaining(["dog", "cat", "fish"], "z"), [])

    def test_multiple_same_word(self):
        self.assertEqual(self.sol.findWordsContaining(["aaa", "bbb", "ccc"], "a"), [0])

    def test_empty_list(self):
        self.assertEqual(self.sol.findWordsContaining([], "a"), [])

    def test_single_char_words(self):
        self.assertEqual(self.sol.findWordsContaining(["a", "b", "c", "a"], "a"), [0, 3])


if __name__ == "__main__":
    unittest.main()

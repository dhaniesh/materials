"""
1768. Merge Strings Alternately

You are given two strings `word1` and `word2`. Merge the strings by adding letters in alternating order, 
starting with `word1`. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

Example 1:
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"

Example 2:
Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"

Example 3:
Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"

Constraints:
- 1 <= word1.length, word2.length <= 100
- word1 and word2 consist of lowercase English letters.
"""

from typing import List
import unittest

"""
Approach:
- merge alternalively until both the pointers are < len
- merge the remaining string

"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p = q = 0
        merged = ""
        while p < len(word1) and q < len(word2):
            merged += word1[p] + word2[q]
            p += 1
            q += 1
        merged += word1[p:] + word2[q:]
        return merged

class TestMergeStringsAlternately(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.mergeAlternately("abc", "pqr"), "apbqcr")

    def test_example_2(self):
        self.assertEqual(self.solution.mergeAlternately("ab", "pqrs"), "apbqrs")

    def test_example_3(self):
        self.assertEqual(self.solution.mergeAlternately("abcd", "pq"), "apbqcd")

    def test_one_empty(self):
        self.assertEqual(self.solution.mergeAlternately("", "xyz"), "xyz")

    def test_both_empty(self):
        self.assertEqual(self.solution.mergeAlternately("", ""), "")

if __name__ == "__main__":
    unittest.main()

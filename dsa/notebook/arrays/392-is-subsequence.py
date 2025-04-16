"""
392. Is Subsequence

Given two strings `s` and `t`, return true if `s` is a subsequence of `t`, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) 
of the characters without disturbing the relative positions of the remaining characters. 
(ie., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false

Constraints:
- 0 <= s.length <= 100
- 0 <= t.length <= 10⁴
- `s` and `t` consist only of lowercase English letters.

Follow up: If there are lots of incoming `s`, say `s1, s2, ..., sk` where k >= 10⁹, 
and you want to check one by one to see if `t` has each of them as a subsequence, 
in what way could you optimize your algorithm?
"""

import unittest

"""
Approach:

- two pointers

"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)

class TestIsSubsequence(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertTrue(self.solution.isSubsequence("abc", "ahbgdc"))

    def test_example_2(self):
        self.assertFalse(self.solution.isSubsequence("axc", "ahbgdc"))

    def test_empty_s(self):
        self.assertTrue(self.solution.isSubsequence("", "ahbgdc"))

    def test_s_longer_than_t(self):
        self.assertFalse(self.solution.isSubsequence("abc", "ab"))

    def test_same_string(self):
        self.assertTrue(self.solution.isSubsequence("abc", "abc"))

if __name__ == "__main__":
    unittest.main()

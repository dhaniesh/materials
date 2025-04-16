"""
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:
- 1 <= strs.length <= 200
- 0 <= strs[i].length <= 200
- strs[i] consists of only lowercase English letters.
"""

from typing import List
import unittest

"""
Approach:

- calculate prefix for adjacent word

"""


class Solution:
    def commonPrefix(self, p, q):
        i = 0
        prefix = ''
        while i < len(p) and i < len(q):
            if p[i] == q[i]:
                prefix += p[i]
                i += 1
            else:
                break
        return prefix

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for word in strs:
            prefix = self.commonPrefix(prefix, word)
        return prefix


class TestLongestCommonPrefix(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.longestCommonPrefix(
            ["flower", "flow", "flight"]), "fl")

    def test_example_2(self):
        self.assertEqual(self.solution.longestCommonPrefix(
            ["dog", "racecar", "car"]), "")

    def test_all_same(self):
        self.assertEqual(self.solution.longestCommonPrefix(
            ["test", "test", "test"]), "test")

    def test_single_word(self):
        self.assertEqual(self.solution.longestCommonPrefix(["alone"]), "alone")

    def test_empty_string_in_list(self):
        self.assertEqual(self.solution.longestCommonPrefix(["", "b", "c"]), "")

    def test_mixed_lengths(self):
        self.assertEqual(self.solution.longestCommonPrefix(
            ["interstellar", "internet", "internal"]), "inter")


if __name__ == "__main__":
    unittest.main()

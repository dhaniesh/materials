"""
LeetCode Problem: Minimum Window Substring

Given two strings s and t, return the minimum window substring of s
such that every character in t (including duplicates) is included in the window.
If there is no such substring, return an empty string "".

Examples:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"

Input: s = "a", t = "a"
Output: "a"

Input: s = "a", t = "aa"
Output: ""
"""

import unittest
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        window = {}
        have, needCount = 0, len(need)
        res, resLen = [-1, -1], float("inf")
        left = 0

        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1

            if c in need and window[c] == need[c]:
                have += 1

            while have == needCount:
                # Update result window
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = right - left + 1

                # Shrink from left
                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1
                left += 1

        l, r = res
        return s[l:r + 1] if resLen != float("inf") else ""


class TestMinWindowSubstring(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_example_case(self):
        self.assertEqual(
            self.sol.minWindow("ADOBECODEBANC", "ABC"),
            "BANC"
        )

    def test_exact_match(self):
        self.assertEqual(
            self.sol.minWindow("a", "a"),
            "a"
        )

    def test_no_possible_window(self):
        self.assertEqual(
            self.sol.minWindow("a", "aa"),
            ""
        )

    def test_repeated_characters(self):
        self.assertEqual(
            self.sol.minWindow("aaabbbc", "abc"),
            "abbbc"
        )

    def test_window_at_start(self):
        self.assertEqual(
            self.sol.minWindow("abcde", "abc"),
            "abc"
        )

    def test_window_at_end(self):
        self.assertEqual(
            self.sol.minWindow("xyzabc", "abc"),
            "abc"
        )


if __name__ == "__main__":
    unittest.main()


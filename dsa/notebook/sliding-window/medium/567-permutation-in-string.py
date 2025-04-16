"""
567. Permutation in String (Medium)

Given two strings s1 and s2, return true if s2 contains a permutation of s1.

In other words, return true if one of the first string's permutations is the substring of the second string.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false

Constraints:
- 1 <= s1.length, s2.length <= 10⁴
- s1 and s2 consist of lowercase English letters.
"""

import unittest

"""
Approach:
We can use the sliding window technique to check for permutations of s1 within s2 by maintaining character 
counts and adjusting the window size as we go along.
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        pass

class TestPermutationInString(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertTrue(self.solution.checkInclusion("ab", "eidbaooo"))

    def test_example_2(self):
        self.assertFalse(self.solution.checkInclusion("ab", "eidboaoo"))

if __name__ == "__main__":
    unittest.main()

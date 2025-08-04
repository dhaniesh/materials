"""
205. Isomorphic Strings (Easy)

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t. 
All occurrences of a character in s must be replaced with the same character in t, 
and no two characters may map to the same character.

Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true

Constraints:
- 1 <= s.length <= 5 * 10⁴
- t.length == s.length
- s and t consist of any valid ASCII character.
"""

import unittest

"""
Approach:
We can use two hash maps to track the mappings between characters in s and t. If we find an inconsistency 
in the mapping, we return false.
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        pass

class TestIsomorphicStrings(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertTrue(self.solution.isIsomorphic("egg", "add"))

    def test_example_2(self):
        self.assertFalse(self.solution.isIsomorphic("foo", "bar"))

    def test_example_3(self):
        self.assertTrue(self.solution.isIsomorphic("paper", "title"))

if __name__ == "__main__":
    unittest.main()

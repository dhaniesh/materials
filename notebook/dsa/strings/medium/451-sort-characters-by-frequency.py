"""
451. Sort Characters by Frequency (Medium)

Given a string s, sort it in decreasing order based on the frequency of the characters. 
The frequency of a character is the number of times it appears in the string. 
Return the sorted string.

Example 1:
Input: s = "tree"
Output: "eert"

Example 2:
Input: s = "cccaaa"
Output: "aaaccc"

Example 3:
Input: s = "Aabb"
Output: "bbAa"

Constraints:
- 1 <= s.length <= 5 * 10⁵
- s consists of English letters (uppercase and lowercase), digits, and symbols.
"""

import unittest
from collections import Counter

"""
Approach:
We can use a Counter to count the frequency of each character, 
then sort the characters based on their frequency in descending order. 
Finally, we can join the characters to form the result.
"""

class Solution:
    def frequencySort(self, s: str) -> str:
        pass

class TestSortCharactersByFrequency(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        s = "tree"
        self.assertEqual(self.solution.frequencySort(s), "eert")

    def test_example_2(self):
        s = "cccaaa"
        self.assertEqual(self.solution.frequencySort(s), "aaaccc")

    def test_example_3(self):
        s = "Aabb"
        self.assertEqual(self.solution.frequencySort(s), "bbAa")

    def test_single_character(self):
        s = "a"
        self.assertEqual(self.solution.frequencySort(s), "a")

    def test_all_unique_characters(self):
        s = "abcdef"
        self.assertEqual(self.solution.frequencySort(s), "abcdef")

if __name__ == "__main__":
    unittest.main()

"""
151. Reverse Words in a String (Medium)

Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in the input string will be separated by a single space.

Return a string of the words in reverse order.

Example 1:
Input: s = "the sky is blue"
Output: "blue is sky the"

Example 2:
Input: s = "  hello world  "
Output: "world hello"

Example 3:
Input: s = "a good   example"
Output: "example good a"

Constraints:
- 1 <= s.length <= 10⁴
- s contains English letters (upper-case and lower-case), digits, and spaces.
- There is at least one word in s.
"""

import unittest

"""
Approach:
The idea is to split the string into words, reverse the list of words, 
and then join them back together. We should also handle the extra spaces.
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        pass

class TestReverseWords(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        s = "the sky is blue"
        self.assertEqual(self.solution.reverseWords(s), "blue is sky the")

    def test_example_2(self):
        s = "  hello world  "
        self.assertEqual(self.solution.reverseWords(s), "world hello")

    def test_example_3(self):
        s = "a good   example"
        self.assertEqual(self.solution.reverseWords(s), "example good a")

    def test_single_word(self):
        s = "hello"
        self.assertEqual(self.solution.reverseWords(s), "hello")

    def test_empty_string(self):
        s = "   "
        self.assertEqual(self.solution.reverseWords(s), "")

if __name__ == "__main__":
    unittest.main()

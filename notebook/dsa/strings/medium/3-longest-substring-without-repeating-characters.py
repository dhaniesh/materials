"""
3. Longest Substring Without Repeating Characters (Medium)

Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. Notice that the answer must be a substring, 
"pwke" is a subsequence and not a substring.

Constraints:
- 0 <= s.length <= 5 * 10⁴
- s consists of English letters, digits, symbols, and spaces.
"""

import unittest

"""
Approach:
We can use the sliding window technique to find the longest substring without repeating characters. 
The idea is to maintain a window of characters that are unique and adjust the window boundaries 
when a repeated character is found.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pass

class TestLongestSubstringWithoutRepeatingCharacters(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        s = "abcabcbb"
        self.assertEqual(self.solution.lengthOfLongestSubstring(s), 3)

    def test_example_2(self):
        s = "bbbbb"
        self.assertEqual(self.solution.lengthOfLongestSubstring(s), 1)

    def test_example_3(self):
        s = "pwwkew"
        self.assertEqual(self.solution.lengthOfLongestSubstring(s), 3)

    def test_empty_string(self):
        s = ""
        self.assertEqual(self.solution.lengthOfLongestSubstring(s), 0)

    def test_single_character(self):
        s = "a"
        self.assertEqual(self.solution.lengthOfLongestSubstring(s), 1)

if __name__ == "__main__":
    unittest.main()

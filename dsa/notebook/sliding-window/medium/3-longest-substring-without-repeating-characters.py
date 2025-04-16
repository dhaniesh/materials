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
Explanation: The answer is "wke", with the length of 3.

Constraints:
- 1 <= s.length <= 10⁵
- s consists of English letters, digits, symbols, and spaces.
"""

import unittest

"""
Approach:
We can use the sliding window technique with a set or hash map to efficiently track unique characters 
and update the window boundaries accordingly.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pass

class TestLongestSubstring(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("abcabcbb"), 3)

    def test_example_2(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("bbbbb"), 1)

    def test_example_3(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("pwwkew"), 3)

if __name__ == "__main__":
    unittest.main()

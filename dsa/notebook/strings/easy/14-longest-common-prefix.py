"""
14. Longest Common Prefix (Easy)

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""

Example 3:
Input: strs = ["interstellar", "internet", "internal"]
Output: "inte"

Constraints:
- 1 <= strs.length <= 200
- 0 <= strs[i].length <= 200
- strs[i] consists of only lowercase English letters.
"""

import unittest

"""
Approach:
The idea is to compare characters of the strings one by one, 
starting from the first character. If all strings have the same character at a position, 
add it to the result. If we find a mismatch, return the current prefix.
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pass

class TestLongestCommonPrefix(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        strs = ["flower", "flow", "flight"]
        self.assertEqual(self.solution.longestCommonPrefix(strs), "fl")

    def test_example_2(self):
        strs = ["dog", "racecar", "car"]
        self.assertEqual(self.solution.longestCommonPrefix(strs), "")

    def test_example_3(self):
        strs = ["interstellar", "internet", "internal"]
        self.assertEqual(self.solution.longestCommonPrefix(strs), "inte")

    def test_single_string(self):
        strs = ["single"]
        self.assertEqual(self.solution.longestCommonPrefix(strs), "single")

    def test_empty_list(self):
        strs = []
        self.assertEqual(self.solution.longestCommonPrefix(strs), "")

if __name__ == "__main__":
    unittest.main()

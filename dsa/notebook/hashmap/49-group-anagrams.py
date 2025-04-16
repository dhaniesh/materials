"""
49. Group Anagrams (Medium)

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
"""

import unittest

"""
Approach:
Use a hashmap to group words by their sorted character tuple.
All anagrams will have the same sorted tuple of characters.
"""

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        pass

class TestGroupAnagrams(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        input_data = ["eat","tea","tan","ate","nat","bat"]
        output = self.solution.groupAnagrams(input_data)
        self.assertTrue(any(set(group) == {"eat", "tea", "ate"} for group in output))
        self.assertTrue(any(set(group) == {"tan", "nat"} for group in output))
        self.assertTrue(any(set(group) == {"bat"} for group in output))

    def test_example_2(self):
        input_data = [""]
        self.assertEqual(self.solution.groupAnagrams(input_data), [[""]])

    def test_example_3(self):
        input_data = ["a"]
        self.assertEqual(self.solution.groupAnagrams(input_data), [["a"]])

if __name__ == "__main__":
    unittest.main()

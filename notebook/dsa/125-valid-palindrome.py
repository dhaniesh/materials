"""
125. Valid Palindrome
---------------------------------
Given a string `s`, determine if it is a palindrome,
considering only alphanumeric characters and ignoring cases.

A string is a palindrome when it reads the same backward as forward,
after removing non-alphanumeric characters and ignoring case.

Example 1:
    Input: s = "A man, a plan, a canal: Panama"
    Output: True
    Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
    Input: s = "race a car"
    Output: False
    Explanation: "raceacar" is not a palindrome.

Example 3:
    Input: s = " "
    Output: True
    Explanation: An empty string after filtering is a palindrome.

Approach:
---------------------------------
1. Normalize the input:
   - Convert all characters to lowercase.
   - Keep only alphanumeric characters.
2. Use two-pointer technique:
   - Initialize `left` at start and `right` at end of string.
   - Move pointers inward while characters match.
   - If mismatch occurs, return False.
3. If pointers meet or cross, return True.
"""

import unittest

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c.lower() for c in s if c.isalnum())
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


class TestIsPalindrome(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_basic_palindrome(self):
        self.assertTrue(self.sol.isPalindrome("madam"))
        self.assertTrue(self.sol.isPalindrome("abba"))
        self.assertFalse(self.sol.isPalindrome("abc"))

    def test_with_spaces_and_punctuation(self):
        self.assertTrue(self.sol.isPalindrome("A man, a plan, a canal: Panama"))
        self.assertFalse(self.sol.isPalindrome("race a car"))

    def test_empty_and_single_char(self):
        self.assertTrue(self.sol.isPalindrome(""))
        self.assertTrue(self.sol.isPalindrome(" "))
        self.assertTrue(self.sol.isPalindrome("a"))

    def test_mixed_characters(self):
        self.assertTrue(self.sol.isPalindrome("No 'x' in Nixon"))
        self.assertFalse(self.sol.isPalindrome("hello!"))
        self.assertTrue(self.sol.isPalindrome("Able , was I saw eLba"))

    def test_numeric_cases(self):
        self.assertTrue(self.sol.isPalindrome("12321"))
        self.assertFalse(self.sol.isPalindrome("12345"))
        self.assertTrue(self.sol.isPalindrome("1a2a1"))


if __name__ == "__main__":
    unittest.main()

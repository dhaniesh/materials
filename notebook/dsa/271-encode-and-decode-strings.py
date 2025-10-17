"""
Title: Encode and Decode Strings
Problem:
Design an algorithm to encode a list of strings to a single string,
and decode it back to the original list.

Example:
Input: ["leet", "code"]
Output after encode: "4#leet4#code"
Decoded output: ["leet", "code"]

Approach:
Use length-prefix encoding: "<len>#<string>" for each word.
"""

import unittest


class Solution:
    def encode(self, strs):
        """Encodes a list of strings into a single string."""
        encoded_string = ""
        for s in strs:
            encoded_string += str(len(s)) + "#" + s
        return encoded_string

    def decode(self, s):
        """Decodes a single string back into a list of strings."""
        decoded_string_list = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            word = s[j+1: j+1+length]
            decoded_string_list.append(word)
            i = j+1 + length
        return decoded_string_list


# ------------------ Unit Tests ------------------

class TestEncodeDecode(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic(self):
        data = ["leet", "code", "love", "you"]
        encoded = self.solution.encode(data)
        decoded = self.solution.decode(encoded)
        self.assertEqual(decoded, data)

    def test_empty_strings(self):
        data = ["", "", "a", ""]
        encoded = self.solution.encode(data)
        decoded = self.solution.decode(encoded)
        self.assertEqual(decoded, data)

    def test_single_word(self):
        data = ["hello"]
        encoded = self.solution.encode(data)
        decoded = self.solution.decode(encoded)
        self.assertEqual(decoded, data)

    def test_with_special_chars(self):
        data = ["a#b", "123#45", "#", ""]
        encoded = self.solution.encode(data)
        decoded = self.solution.decode(encoded)
        self.assertEqual(decoded, data)


if __name__ == "__main__":
    unittest.main()

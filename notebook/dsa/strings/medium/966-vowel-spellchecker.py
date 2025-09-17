"""
966. Vowel Spellchecker (Medium)

Given a wordlist, we want to implement a spellchecker that converts a query word into a correct word.

The spellchecker handles two categories of spelling mistakes:

1. Capitalization: If the query matches a word in the wordlist case-insensitively, 
   then return the first such match in the wordlist.

2. Vowel Errors: If after replacing all vowels ('a', 'e', 'i', 'o', 'u') with '*', 
   the query matches a word in the wordlist (case-insensitive), then return the first such match.

If the query matches exactly, return the query itself. If no match found, return empty string.

Example:

Input: wordlist = ["KiTe","kite","hare","Hare"], queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti"]
Output: ["kite","KiTe","KiTe","Hare","hare","","","KiTe"]

Constraints:
- 1 <= wordlist.length, queries.length <= 5000
- 1 <= wordlist[i].length, queries[i].length <= 7
- All strings consist only of English letters.
"""

from typing import List
import unittest

"""
Approach:
- Use three data structures for quick lookups:
  1. exact_words: set of original words for exact match
  2. case_insensitive: dict mapping lowercased words to the first occurrence word in wordlist
  3. vowel_masked: dict mapping vowel-masked words to the first occurrence word

- For each query:
  - If exact match exists, return it.
  - Else if case-insensitive match exists, return that.
  - Else if vowel error match exists, return that.
  - Otherwise, return "".
"""

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def devowel(word: str) -> str:
            vowels = set('aeiou')
            return ''.join('*' if c in vowels else c for c in word.lower())
        
        exact_words = set(wordlist)
        case_insensitive = {}
        vowel_masked = {}
        
        for word in wordlist:
            low = word.lower()
            case_insensitive.setdefault(low, word)
            vowel_masked.setdefault(devowel(word), word)
        
        result = []
        for query in queries:
            if query in exact_words:
                result.append(query)
            else:
                low = query.lower()
                if low in case_insensitive:
                    result.append(case_insensitive[low])
                else:
                    devow = devowel(query)
                    if devow in vowel_masked:
                        result.append(vowel_masked[devow])
                    else:
                        result.append("")
        return result

class TestSpellchecker(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_examples(self):
        wordlist = ["KiTe","kite","hare","Hare"]
        queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti"]
        expected = ["kite","KiTe","KiTe","Hare","hare","","","KiTe"]
        self.assertEqual(self.solution.spellchecker(wordlist, queries), expected)

if __name__ == "__main__":
    unittest.main()

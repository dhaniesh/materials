"""
763. Partition Labels (Medium)

You are given a string s. You want to partition the string into as many parts as possible 
so that each letter appears in at most one part. Return a list of integers representing the 
size of these parts.

Example:
Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
  - The first partition is "ababcbaca" (9 letters), which contains all occurrences of 'a', 'b', and 'c'.
  - The second partition is "defegde" (7 letters).
  - The third is "hijhklij" (8 letters).
"""

import unittest

"""
Approach 1:
- count, iterate over the original s
- use a set and add elements, dec the counter at every iteration
- whenever the counter[char] becomes zero, remove from set and check if set is empty
- if yes, we have a valid substr, return the result of all substr

Approach 1:
- use a dict to track all the rightmost index of a character
- for every iteration, find out the max right of the window
- if i == calculated right, append to result, update left to right + 1
"""

class Solution:
    
    def partitionLabels(self, s: str):
        result = []
        l = r = 0
        rightmost = {}
        for i, c in enumerate(s):
            rightmost[c] = i
        
        for i, c in enumerate(s):
            r = max(r, rightmost[c])

            if i == r:
                result.append(r-l+1)
                l = r + 1
        return result
 
        

    def partitionLabels_(self, s: str) -> list[int]:
        result = []
        count = {}
        size = 0
        for c in s:
            count[c] = 1 + count.get(c, 0)
        
        pool = set()
        for c in s:
            pool.add(c)
            size += 1
            count[c] -= 1
            if count[c] == 0:
                pool.remove(c)
                if not pool:
                    result.append(size)
                    size = 0
        return result


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        s = "ababcbacadefegdehijhklij"
        self.assertEqual(self.sol.partitionLabels(s), [9, 7, 8])

    def test_example_2(self):
        s = "eccbbbbdec"
        self.assertEqual(self.sol.partitionLabels(s), [10])

    def test_single_char(self):
        s = "a"
        self.assertEqual(self.sol.partitionLabels(s), [1])

    def test_all_unique(self):
        s = "abcdef"
        self.assertEqual(self.sol.partitionLabels(s), [1, 1, 1, 1, 1, 1])

    def test_repeating_block(self):
        s = "aaabbbccc"
        self.assertEqual(self.sol.partitionLabels(s), [3, 3, 3])


if __name__ == '__main__':
    unittest.main()

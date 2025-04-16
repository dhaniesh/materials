"""
278. First Bad Version (Easy)

You are a product manager and have just discovered that one of the versions of your product is faulty. 
Unfortunately, you cannot go back and fix the problem, so you have to find which version is the first bad one.

You have `n` versions [1, 2, ..., n] and you want to find the first bad one, which causes all the following versions to be bad.

You are given an API `isBadVersion(version)` which returns whether version is bad. Implement a solution to find the first bad version.

You should minimize the number of calls to the API.

Example 1:
Input: n = 5, bad = 4
Output: 4

Example 2:
Input: n = 1, bad = 1
Output: 1

Constraints:
- 1 <= bad <= n <= 2³¹ - 1
"""

from typing import List
import unittest

"""
Approach:
The problem can be solved using binary search.
We can divide the range [1, n] into halves and check if the middle version is bad.
If it is, we search in the left half, otherwise, we search in the right half.
"""

class Solution:
    def firstBadVersion(self, n: int) -> int:
        pass

class TestFirstBadVersion(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        n = 5
        bad = 4
        self.assertEqual(self.solution.firstBadVersion(n), 4)

    def test_example_2(self):
        n = 1
        bad = 1
        self.assertEqual(self.solution.firstBadVersion(n), 1)

    def test_large_n(self):
        n = 10**6
        bad = 500000
        self.assertEqual(self.solution.firstBadVersion(n), 500000)

    def test_first_version_bad(self):
        n = 10
        bad = 1
        self.assertEqual(self.solution.firstBadVersion(n), 1)

    def test_last_version_bad(self):
        n = 10
        bad = 10
        self.assertEqual(self.solution.firstBadVersion(n), 10)

if __name__ == "__main__":
    unittest.main()

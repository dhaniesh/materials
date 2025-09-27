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

import unittest

"""
Approach:
The problem can be solved using binary search.
We can divide the range [1, n] into halves and check if the middle version is bad.
If it is, we search in the left half, otherwise, we search in the right half.
"""

# Mockable version control
class VersionControl:
    def __init__(self, bad: int):
        self.bad = bad

    def isBadVersion(self, version: int) -> bool:
        return version >= self.bad


class Solution(VersionControl):
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        while l < r:
            m = (l + r) // 2
            if self.isBadVersion(m):
                r = m
            else:
                l = m + 1
        return l


class TestFirstBadVersion(unittest.TestCase):

    def test_case_1(self):
        sol = Solution(4)
        self.assertEqual(sol.firstBadVersion(5), 4)

    def test_case_single(self):
        sol = Solution(1)
        self.assertEqual(sol.firstBadVersion(1), 1)

    def test_case_middle(self):
        sol = Solution(7)
        self.assertEqual(sol.firstBadVersion(10), 7)

    def test_case_first(self):
        sol = Solution(1)
        self.assertEqual(sol.firstBadVersion(100), 1)

    def test_case_last(self):
        sol = Solution(100)
        self.assertEqual(sol.firstBadVersion(100), 100)


if __name__ == "__main__":
    unittest.main()

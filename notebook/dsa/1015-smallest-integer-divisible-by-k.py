"""
1015. Smallest Integer Divisible by K

Given a positive integer k, return the length of the smallest positive integer n such that the number
composed of n digits of only '1' (i.e., 1, 11, 111, 1111, …) is divisible by k.

If no such n exists, return -1.

Examples:
---------
Input: k = 1 → Output: 1  
Input: k = 3 → Output: 3  
Input: k = 2 → Output: -1

Constraints:
------------
1 <= k <= 10^5

Approach:
---------
Instead of constructing giant numbers of 1s, track the remainder sequence:

Let R(n) be a repunit with n digits.
Then:
    R(n+1) = R(n)*10 + 1
    rem(n+1) = (rem(n)*10 + 1) % k

When rem becomes 0 → divisible → return n.
If a remainder repeats → cycle → return -1.

Time: O(k)  
Space: O(k)
----------------------------------------------------------------------------------------------------
"""

import unittest


class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        # Repunit can't be divisible by numbers containing factor 2 or 5
        if k % 2 == 0 or k % 5 == 0:
            return -1

        rem = 0
        seen = set()
        length = 0

        while rem not in seen:
            seen.add(rem)
            rem = (rem * 10 + 1) % k
            length += 1
            if rem == 0:
                return length

        return -1


class TestSmallestRepunitDivByK(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    # ---------------------------
    # Top 5 Most Important Test Cases
    # ---------------------------

    def test_divisible_1(self):
        # Basic smallest case
        self.assertEqual(self.sol.smallestRepunitDivByK(1), 1)

    def test_divisible_3(self):
        # Classic divisible case: 111 % 3 == 0
        self.assertEqual(self.sol.smallestRepunitDivByK(3), 3)

    def test_not_possible_2(self):
        # Cannot be divisible by 2
        self.assertEqual(self.sol.smallestRepunitDivByK(2), -1)

    def test_not_possible_5(self):
        # Cannot be divisible by 5
        self.assertEqual(self.sol.smallestRepunitDivByK(5), -1)

    def test_large_valid_7(self):
        # Known: 111111 % 7 == 0 → length = 6
        self.assertEqual(self.sol.smallestRepunitDivByK(7), 6)


if __name__ == "__main__":
    unittest.main()


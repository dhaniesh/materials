"""
202. Happy Number

Write an algorithm to determine if a number n is a happy number.

A happy number is defined as:
- Starting with any positive integer, replace the number by the sum of the squares of its digits.
- Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle that does not include 1.
- Those numbers for which this process ends in 1 are happy numbers.

Example 1:
Input: n = 19
Output: True
Explanation: 
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1 → Happy number

Example 2:
Input: n = 2
Output: False
Explanation:
2^2 = 4
4^2 = 16
1^2 + 6^2 = 37
3^2 + 7^2 = 58
5^2 + 8^2 = 89
8^2 + 9^2 = 145
1^2 + 4^2 + 5^2 = 42
4^2 + 2^2 = 20
2^2 + 0^2 = 4 → loops forever → Not happy

Approach:
- Use a set to keep track of seen numbers to detect loops
- If we reach 1 → return True
- If we see a number already seen → return False
"""

import unittest

class Solution:
    def isHappy(self, num: int) -> bool:
        seen = set()
        def resolve(num):
            if num == 1:
                return True
            if num in seen:
                return False
            seen.add(num)
            return resolve(sum(int(n) ** 2 for n in str(num)))
        return resolve(num)


class TestIsHappy(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_happy_numbers(self):
        self.assertTrue(self.sol.isHappy(19))   # classic happy number
        self.assertTrue(self.sol.isHappy(7))    # single-digit happy
        self.assertTrue(self.sol.isHappy(1))    # base case

    def test_unhappy_numbers(self):
        self.assertFalse(self.sol.isHappy(2))   # classic unhappy number
        self.assertFalse(self.sol.isHappy(3))   # small loop
        self.assertFalse(self.sol.isHappy(4))   # loops forever

    def test_large_numbers(self):
        self.assertTrue(self.sol.isHappy(100))  # becomes 1 quickly
        self.assertFalse(self.sol.isHappy(116)) # eventually cycles

if __name__ == "__main__":
    unittest.main()

"""
LeetCode Problem: 875-koko-eating-bananas

Koko loves bananas and wants to eat all piles within H hours. 
Each hour she chooses a pile and eats K bananas from it. 
If a pile has less than K bananas, she eats all of it and that still counts as an hour.

Return the minimum eating speed K such that Koko can finish all piles within H hours.

Example:
Input: piles = [3,6,7,11], H = 8
Output: 4
Explanation:
At K=4, total hours = ceil(3/4)+ceil(6/4)+ceil(7/4)+ceil(11/4) = 1+2+2+3 = 8 hours.
"""

import unittest
import math
from typing import List


class Solution:
    def eat_bananas(self, piles, rate):
        total_time = 0
        for pile in piles:
            total_time += math.ceil(pile / rate)
        return total_time

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)

        while low <= high:
            mid = (low + high) // 2
            total_time = self.eat_bananas(piles, mid)
            if total_time <= h:
                high = mid - 1
            else:
                low = mid + 1
        return low


class TestMinEatingSpeed(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_example_case(self):
        self.assertEqual(self.sol.minEatingSpeed([3, 6, 7, 11], 8), 4)

    def test_single_pile(self):
        self.assertEqual(self.sol.minEatingSpeed([30], 5), 6)

    def test_large_hours(self):
        # If H >= total bananas, rate = 1
        self.assertEqual(self.sol.minEatingSpeed([1, 2, 3], 10), 1)

    def test_tight_hours(self):
        # Must eat full piles each hour
        self.assertEqual(self.sol.minEatingSpeed([10, 10, 10], 3), 10)

    def test_random_case(self):
        self.assertEqual(self.sol.minEatingSpeed([2, 2, 2, 2], 4), 2)

    
if __name__ == "__main__":
    unittest.main()


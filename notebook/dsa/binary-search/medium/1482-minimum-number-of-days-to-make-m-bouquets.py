"""
1482. Minimum Number of Days to Make m Bouquets (Medium)

You are given an integer array `bloomDay`, an integer `m`, and an integer `k`.

You want to make `m` bouquets. To make a bouquet, you need to use `k` adjacent flowers from the garden.

The garden consists of `n` flowers, the `i`-th flower will bloom in `bloomDay[i]` days.

Return the minimum number of days you need to wait to be able to make `m` bouquets from the garden. If it is impossible to make `m` bouquets return -1.

Example 1:
Input: bloomDay = [1,10,3,10,2], m = 3, k = 1  
Output: 3

Example 2:
Input: bloomDay = [1,10,3,10,2], m = 3, k = 2  
Output: -1

Constraints:
- 1 <= bloomDay.length <= 10⁵
- 1 <= bloomDay[i] <= 10⁹
- 1 <= m <= 10⁶
- 1 <= k <= bloomDay.length
"""

from typing import List
import unittest

"""
Approach:


"""

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        pass

class TestMinDaysToMakeBouquets(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        bloomDay = [1, 10, 3, 10, 2]
        m, k = 3, 1
        self.assertEqual(self.solution.minDays(bloomDay, m, k), 3)

    def test_example_2(self):
        bloomDay = [1, 10, 3, 10, 2]
        m, k = 3, 2
        self.assertEqual(self.solution.minDays(bloomDay, m, k), -1)

    def test_exact_fit(self):
        bloomDay = [7, 7, 7, 7, 12, 7, 7]
        m, k = 2, 3
        self.assertEqual(self.solution.minDays(bloomDay, m, k), 12)

    def test_large_values(self):
        bloomDay = [1000000000] * 100000
        m, k = 1, 100000
        self.assertEqual(self.solution.minDays(bloomDay, m, k), 1000000000)

    def test_impossible(self):
        bloomDay = [1, 2, 3, 4, 5]
        m, k = 2, 3
        self.assertEqual(self.solution.minDays(bloomDay, m, k), -1)

if __name__ == "__main__":
    unittest.main()

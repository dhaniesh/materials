"""
1011. Capacity To Ship Packages Within D Days (Medium)

A conveyor belt has packages that must be shipped from one port to another within `days` days.

The i-th package on the conveyor belt has a weight of `weights[i]`. Each day, we load the ship with packages in the order given by `weights`. We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages being shipped within `days` days.

Example 1:
Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5  
Output: 15

Example 2:
Input: weights = [3,2,2,4,1,4], days = 3  
Output: 6

Example 3:
Input: weights = [1,2,3,1,1], days = 4  
Output: 3

Constraints:
- 1 <= weights.length <= 5 * 10⁴
- 1 <= weights[i] <= 500
- 1 <= days <= 500
"""

from typing import List
import unittest

"""
Approach:


"""

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        pass

class TestShipWithinDays(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        weights = [1,2,3,4,5,6,7,8,9,10]
        days = 5
        self.assertEqual(self.solution.shipWithinDays(weights, days), 15)

    def test_example_2(self):
        weights = [3,2,2,4,1,4]
        days = 3
        self.assertEqual(self.solution.shipWithinDays(weights, days), 6)

    def test_example_3(self):
        weights = [1,2,3,1,1]
        days = 4
        self.assertEqual(self.solution.shipWithinDays(weights, days), 3)

    def test_single_package(self):
        weights = [10]
        days = 1
        self.assertEqual(self.solution.shipWithinDays(weights, days), 10)

    def test_all_same_weights(self):
        weights = [5,5,5,5]
        days = 2
        self.assertEqual(self.solution.shipWithinDays(weights, days), 10)

if __name__ == "__main__":
    unittest.main()

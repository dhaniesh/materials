"""
121. Best Time to Buy and Sell Stock

You are given an array `prices` where `prices[i]` is the price of a given stock on the i-th day.

You want to maximize your profit by choosing a single day to buy one stock and 
choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. 
If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6 - 1 = 5.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: No transactions are done and the max profit is 0.

Constraints:
- 1 <= prices.length <= 10⁵
- 0 <= prices[i] <= 10⁴
"""

from typing import List
import unittest

"""
Approach:

- buy the lowest, check profit, and update the max
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = max(prices)
        for price in prices:
            if price < buy:
                buy = price
            else:
                sell = price - buy
                profit = max(profit, sell)
        return profit

class TestBestTimeToBuyAndSellStock(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.maxProfit([7, 1, 5, 3, 6, 4]), 5)

    def test_example_2(self):
        self.assertEqual(self.solution.maxProfit([7, 6, 4, 3, 1]), 0)

    def test_single_day(self):
        self.assertEqual(self.solution.maxProfit([5]), 0)

    def test_fluctuating_prices(self):
        self.assertEqual(self.solution.maxProfit([2, 4, 1]), 2)

    def test_all_same_prices(self):
        self.assertEqual(self.solution.maxProfit([3, 3, 3, 3]), 0)

if __name__ == "__main__":
    unittest.main()

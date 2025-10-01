"""There are numBottles water bottles that are initially full of water. You can exchange numExchange empty water bottles from the market with one full water bottle.
The operation of drinking a full water bottle turns it into an empty bottle.
Given the two integers numBottles and numExchange, return the maximum number of water bottles you can drink.

Example 1:
Input: numBottles = 9, numExchange = 3
Output: 13
Explanation: You can exchange 3 empty bottles to get 1 full water bottle.
Number of water bottles you can drink: 9 + 3 + 1 = 13.

Example 2:
Input: numBottles = 15, numExchange = 4
Output: 19
Explanation: You can exchange 4 empty bottles to get 1 full water bottle. 
Number of water bottles you can drink: 15 + 3 + 1 = 19.

Approach:
- as long as we have bottles, we can check and refill bottles to drink
- empty the bottle, refill the bottle
"""

import unittest


class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drank = 0
        empty = 0
        while numBottles > 0:
            drank += numBottles
            empty += numBottles
            numBottles, empty = empty // numExchange, empty % numExchange
        return drank


class TestWaterBottles(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        self.assertEqual(self.solution.numWaterBottles(9, 3), 13)

    def test_case_2(self):
        self.assertEqual(self.solution.numWaterBottles(15, 4), 19)

if __name__ == "__main__":
    unittest.main()
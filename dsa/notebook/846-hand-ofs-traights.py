"""
846. Hand of Straights (Medium)

Alice has a hand of cards, given as an integer array `hand`, and an integer `groupSize`.

She wants to rearrange the cards into groups where each group has exactly `groupSize` consecutive cards.

Return True if she can do this, or False otherwise.

Example:
Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
Output: True
Explanation: Groups: [1,2,3], [2,3,4], [6,7,8]
"""

from collections import Counter
import unittest


"""
Approach:

- use counter and iterate through the sorted array of the keys in sorted order
- for each card count, check if consecutive cards appear, if not return False
- return True
"""


class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0: return False

        count = {}
        for card in hand:
            count[card] = 1 + count.get(card, 0)
        
        for card in sorted(count.keys()):
            needed = count[card]
            if needed == 0:
                continue
            for i in range(card, card + groupSize):
                count[i] -= needed
                if count[i] < 0:
                    return False
        return True

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
        groupSize = 3
        self.assertTrue(self.sol.isNStraightHand(hand, groupSize))

    def test_example_2(self):
        hand = [1, 2, 3, 4, 5]
        groupSize = 4
        self.assertFalse(self.sol.isNStraightHand(hand, groupSize))

    def test_edge_case(self):
        hand = [1, 2, 3, 4, 5, 6]
        groupSize = 2
        self.assertTrue(self.sol.isNStraightHand(hand, groupSize))

    def test_invalid_input(self):
        hand = [1, 1, 2, 2, 3, 3]
        groupSize = 3
        self.assertTrue(self.sol.isNStraightHand(hand, groupSize))

    def test_duplicate_groups(self):
        hand = [1, 2, 3, 1, 2, 3]
        groupSize = 3
        self.assertTrue(self.sol.isNStraightHand(hand, groupSize))


if __name__ == '__main__':
    unittest.main()

"""
853. Car Fleet

There are n cars traveling to the same destination along a one-lane road. 
The destination is at `target` miles away.

Each car i has:
  - a starting position `position[i]`
  - a constant speed `speed[i]`
All cars are moving toward the target. 

A car cannot pass another car ahead of it, but it can catch up and form a fleet. 
Two cars form a fleet when the car behind catches up to the one ahead (or moves at the same speed after catching up).
The fleet travels together at the slower car’s speed.

We need to return the total number of car fleets that will arrive at the destination.

Example:
----------
Input:
    target = 12
    position = [10, 8, 0, 5, 3]
    speed = [2, 4, 1, 1, 3]

Output:
    3

Explanation:
  Cars at positions 10 & 8 arrive at the same time (1 hr → 1 fleet)
  Car at position 5 → 7 hrs
  Cars at positions 3 & 0 form a fleet → 3 hrs & 12 hrs → eventually merge
  Total Fleets = 3

Approach:
- zip and sort in reverse
- calculate time of each position, if position x (from 10 to reach 12) takes 2 seconds, and position y (from 8 to 12) takes 1 second, y will reach x passing it, so in this case, it gets grouped
- so for every farthest position p0, it's next position p1 has to take more time than p0 to arrive distinctly 
"""

import unittest
from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        stack = []
        for p, s in cars:
            time = (target - p) / s
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)


class TestCarFleet(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_example_case(self):
        self.assertEqual(
            self.sol.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]),
            3
        )

    def test_single_car(self):
        self.assertEqual(
            self.sol.carFleet(10, [3], [3]),
            1
        )

    def test_no_merge(self):
        # Cars so far apart they never meet
        self.assertEqual(
            self.sol.carFleet(100, [0, 50], [1, 1]),
            2
        )

    def test_all_merge(self):
        # All catch up -> single fleet
        self.assertEqual(
            self.sol.carFleet(100, [10, 20, 30], [3, 2, 1]),
            1
        )

    def test_edge_case_empty(self):
        self.assertEqual(
            self.sol.carFleet(10, [], []),
            0
        )


if __name__ == "__main__":
    unittest.main()


"""
42. Trapping Rain Water (Hard)

Given n non-negative integers representing the height of walls where the width of each wall is 1, 
compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The water trapped in the image above is 6 units.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:
- n == height.length
- 1 <= n <= 2 * 10⁴
- 0 <= height[i] <= 10⁵
"""

import unittest

"""
Approach:
We can use the two-pointer technique to solve this problem in linear time. 
The idea is to maintain two pointers, left and right, and calculate the maximum height from the left and right. 
At each step, we calculate how much water can be trapped at the current index by using the minimum of the 
maximum heights on both sides.
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        pass

class TestTrappingRainWater(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        height = [0,1,0,2,1,0,1,3,2,1,2,1]
        self.assertEqual(self.solution.trap(height), 6)

    def test_example_2(self):
        height = [4,2,0,3,2,5]
        self.assertEqual(self.solution.trap(height), 9)

    def test_single_element(self):
        height = [0]
        self.assertEqual(self.solution.trap(height), 0)

    def test_no_trapping(self):
        height = [1,1,1,1]
        self.assertEqual(self.solution.trap(height), 0)

    def test_ascending_and_descending(self):
        height = [1,2,3,4,5,4,3,2,1]
        self.assertEqual(self.solution.trap(height), 0)

if __name__ == "__main__":
    unittest.main()

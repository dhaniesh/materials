"""
2149. Rearrange Array Elements by Sign

You are given a 0-indexed integer array `nums` of even length consisting of an equal number of positive and negative integers.

You should rearrange the elements of `nums` such that the modified array follows the given conditions:
- Every consecutive pair of integers have opposite signs.
- For all integers with the same sign, the order in which they were present in `nums` is preserved.
- The rearranged array begins with a positive integer.

Return the modified array after rearranging the elements to satisfy the aforementioned conditions.

Example 1:
Input: nums = [3,1,-2,-5,2,-4]
Output: [3,-2,1,-5,2,-4]
Explanation: The positive integers in nums are [3,1,2]. The negative integers are [-2,-5,-4]. 
The only possible way to rearrange them such that they satisfy all conditions is [3,-2,1,-5,2,-4].

Example 2:
Input: nums = [-1,1]
Output: [1,-1]
Explanation: The positive integer is [1]. The negative integer is [-1]. 
They are rearranged as [1,-1].

Constraints:
- 2 <= nums.length <= 2 * 10⁵
- nums.length is even
- 1 <= |nums[i]| <= 10⁵
- nums consists of equal number of positive and negative integers.
"""

from typing import List
import unittest

"""
Approach:
- new array,
- use pointers for positive and negative

"""


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        pos = 0
        neg = 1
        for num in nums:
            if num > 0:
                result[pos] = num
                pos += 2
            else:
                result[neg] = num
                neg += 2
        return result


class TestRearrangeArray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(
            self.solution.rearrangeArray([3, 1, -2, -5, 2, -4]),
            [3, -2, 1, -5, 2, -4]
        )

    def test_example_2(self):
        self.assertEqual(
            self.solution.rearrangeArray([-1, 1]),
            [1, -1]
        )

    def test_alternating_input(self):
        self.assertEqual(
            self.solution.rearrangeArray([1, -1, 2, -2]),
            [1, -1, 2, -2]
        )

    def test_all_positives_first(self):
        self.assertEqual(
            self.solution.rearrangeArray([4, 5, 6, -1, -2, -3]),
            [4, -1, 5, -2, 6, -3]
        )

    def test_all_negatives_first(self):
        self.assertEqual(
            self.solution.rearrangeArray([-1, -2, -3, 1, 2, 3]),
            [1, -1, 2, -2, 3, -3]
        )


if __name__ == "__main__":
    unittest.main()

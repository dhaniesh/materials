import unittest
from typing import List


class Solution:
    # Brute force: sort and calculate
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = sorted(nums1 + nums2)
        length = len(merged)

        if length % 2 == 0:
            return (merged[length // 2] + merged[length // 2 - 1]) / 2
        else:
            return merged[length // 2]


class TestFindMedianSortedArrays(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_odd_total_length(self):
        self.assertEqual(
            self.solution.findMedianSortedArrays([1, 3], [2]),
            2
        )

    def test_even_total_length(self):
        self.assertEqual(
            self.solution.findMedianSortedArrays([1, 2], [3, 4]),
            2.5
        )

    def test_one_array_empty(self):
        self.assertEqual(
            self.solution.findMedianSortedArrays([], [1]),
            1
        )

    def test_both_arrays_single_element(self):
        self.assertEqual(
            self.solution.findMedianSortedArrays([1], [2]),
            1.5
        )

    def test_arrays_with_duplicates(self):
        self.assertEqual(
            self.solution.findMedianSortedArrays([1, 2, 2], [2, 2, 3]),
            2
        )

    def test_negative_numbers(self):
        self.assertEqual(
            self.solution.findMedianSortedArrays([-5, -3], [-2, -1]),
            -2.5
        )

    def test_large_numbers(self):
        self.assertEqual(
            self.solution.findMedianSortedArrays([1000000], [1000001]),
            1000000.5
        )


if __name__ == "__main__":
    unittest.main()

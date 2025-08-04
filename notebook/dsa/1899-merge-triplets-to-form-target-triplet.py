"""
1899. Merge Triplets to Form Target Triplet (Medium)

You are given a list of triplets and a target triplet.
Return True if you can form the target triplet by merging a subset of triplets.

To merge triplets, for each index i (0 ≤ i ≤ 2), take the maximum value at index i from the selected triplets.
"""

import unittest

"""
Approach:

- Filter out triplets where any number is greater than the corresponding number in the target triplet.
- Among the valid triplets, check if you can form the target triplet by taking the max of each index.
"""

class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        a = b = c = 0
        for x, y, z in triplets:
            if x <= target[0] and y <= target[1] and z <= target[2]:
                a, b, c = max(a, x), max(b, y), max(c, z)
        return [a, b, c] == target
        
        


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        triplets = [[2, 5, 3], [1, 8, 4], [1, 7, 5]]
        target = [2, 7, 5]
        self.assertTrue(self.sol.mergeTriplets(triplets, target))

    def test_example_2(self):
        triplets = [[3, 4, 5], [4, 5, 6]]
        target = [3, 2, 5]
        self.assertFalse(self.sol.mergeTriplets(triplets, target))

    def test_edge_case(self):
        triplets = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
        target = [3, 3, 3]
        self.assertTrue(self.sol.mergeTriplets(triplets, target))

if __name__ == "__main__":
    unittest.main()

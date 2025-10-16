"""
Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Approach:
1. Count frequencies using Counter.
2. Push elements into a max-heap (using negative frequency).
3. Pop the top k elements for the result.
"""

from typing import List
import unittest

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        import heapq

        result = []
        heap = []
        counter = Counter(nums)

        for num, count in counter.items():
            heapq.heappush(heap, (-count, num))  # negative count for max heap

        while k > 0 and heap:
            result.append(heapq.heappop(heap)[1])
            k -= 1

        return result


class TestTopKFrequent(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertCountEqual(self.sol.topKFrequent([1,1,1,2,2,3], 2), [1,2])

    def test_example2(self):
        self.assertEqual(self.sol.topKFrequent([1], 1), [1])

    def test_all_unique(self):
        self.assertCountEqual(self.sol.topKFrequent([4,5,6,7], 2), [4,5])

    def test_large_counts(self):
        self.assertCountEqual(self.sol.topKFrequent([1,2,2,3,3,3,4,4,4,4], 1), [4])

    def test_negative_numbers(self):
        self.assertCountEqual(self.sol.topKFrequent([-1,-1,-2,-3,-3], 2), [-1,-3])


if __name__ == "__main__":
    unittest.main()

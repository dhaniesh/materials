import unittest
from typing import List

class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        partition = 0
        left_sum = 0
        right_sum = sum(nums)
        for num in nums:
            left_sum += num
            right_sum -= num
            if left_sum and right_sum and (left_sum - right_sum) % 2 == 0:
                partition += 1
        return partition


class TestCountPartitions(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_case_1(self):
        nums = [1, 2]
        self.assertEqual(self.sol.countPartitions(nums), 0)

    def test_case_2(self):
        nums = [5, 5, 5, 5]
        self.assertEqual(self.sol.countPartitions(nums), 3)

    def test_case_3(self):
        nums = [1] * 10  # valid (length <= 100, values 1–100)
        self.assertEqual(self.sol.countPartitions(nums), 9)


if __name__ == "__main__":
    unittest.main()

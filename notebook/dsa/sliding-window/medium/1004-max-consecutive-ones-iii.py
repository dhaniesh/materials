"""
1004. Max Consecutive Ones III (Medium)

Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array 
if you can flip at most k 0's.

Example 1:
Input: nums = [1,1,0,0,1,1,1,0,1,1], k = 2
Output: 6
Explanation: [1,1,1,1,1,1] is the longest subarray with at most 2 flips.

Example 2:
Input: nums = [0,0,1,1,1,0,0,1,1,0], k = 1
Output: 4
Explanation: [1,1,1,1] is the longest subarray with at most 1 flip.

Constraints:
- 1 <= nums.length <= 10⁵
- 0 <= k <= nums.length
- nums[i] is either 0 or 1.
"""

import unittest

"""
Approach:
We can solve this problem using the sliding window (two-pointer) technique. We will maintain a window of 1's 
and 0's, and whenever the number of 0's in the window exceeds k, we shrink the window from the left. 
This ensures that we are flipping at most k 0's in the subarray.
"""

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        pass

class TestMaxConsecutiveOnesIII(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [1, 1, 0, 0, 1, 1, 1, 0, 1, 1]
        k = 2
        self.assertEqual(self.solution.longestOnes(nums, k), 6)

    def test_example_2(self):
        nums = [0, 0, 1, 1, 1, 0, 0, 1, 1, 0]
        k = 1
        self.assertEqual(self.solution.longestOnes(nums, k), 4)

    def test_single_1s_only(self):
        nums = [1, 1, 1, 1]
        k = 2
        self.assertEqual(self.solution.longestOnes(nums, k), 4)

    def test_single_0s_only(self):
        nums = [0, 0, 0, 0, 0]
        k = 2
        self.assertEqual(self.solution.longestOnes(nums, k), 4)

    def test_all_zeros_with_flips(self):
        nums = [0, 0, 0, 0, 0]
        k = 3
        self.assertEqual(self.solution.longestOnes(nums, k), 4)

if __name__ == "__main__":
    unittest.main()

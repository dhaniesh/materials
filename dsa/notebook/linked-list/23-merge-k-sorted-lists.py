"""
23. Merge K Sorted Lists (Hard)

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []
"""

import unittest

"""
Approach:
We can use a min-heap (priority queue) to efficiently merge the k sorted lists.
Each time we pop from the heap, we add the next node from the corresponding list into the heap.
"""

import heapq

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        pass

class TestMergeKSortedLists(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        lists = [
            ListNode(1, ListNode(4, ListNode(5))),
            ListNode(1, ListNode(3, ListNode(4))),
            ListNode(2, ListNode(6))
        ]
        result = self.solution.mergeKLists(lists)
        self.assertEqual(result.val, 1)
        self.assertEqual(result.next.val, 1)

    def test_example_2(self):
        lists = []
        result = self.solution.mergeKLists(lists)
        self.assertIsNone(result)

    def test_example_3(self):
        lists = [None]
        result = self.solution.mergeKLists(lists)
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()

"""
21. Merge Two Sorted Lists (Easy)

Merge two sorted linked lists and return it as a new sorted list. 
The new list should be made by splicing together the nodes of the first two lists.

Example 1:
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: l1 = [], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [], l2 = []
Output: []
"""

import unittest

"""
Approach:
We will iterate through both linked lists, comparing their current nodes and attaching the smaller node to the result.
We continue this process until one list is exhausted, then we attach the remaining nodes of the other list.
"""

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        pass

class TestMergeTwoSortedLists(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        l1 = ListNode(1, ListNode(2, ListNode(4)))
        l2 = ListNode(1, ListNode(3, ListNode(4)))
        result = self.solution.mergeTwoLists(l1, l2)
        self.assertEqual(result.val, 1)
        self.assertEqual(result.next.val, 1)

    def test_example_2(self):
        l1 = None
        l2 = ListNode(0)
        result = self.solution.mergeTwoLists(l1, l2)
        self.assertEqual(result.val, 0)

if __name__ == "__main__":
    unittest.main()

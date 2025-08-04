"""
143. Reorder List (Medium)

Given a singly linked list, reorder it such that the nodes are rearranged in the following order:
L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...

You must do this in-place without altering the nodes' values.

Example 1:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

Example 2:
Input: head = [1,2,3,4]
Output: [1,4,2,3]
"""

import unittest

"""
Approach:
We first split the linked list into two halves. Then we reverse the second half of the list 
and merge the two halves together, alternating nodes from each half.
"""

class Solution:
    def reorderList(self, head: ListNode) -> None:
        pass

class TestReorderList(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        result = self.solution.reorderList(head)
        self.assertEqual(result.val, 1)
        self.assertEqual(result.next.val, 5)
        self.assertEqual(result.next.next.val, 2)
        self.assertEqual(result.next.next.next.val, 4)

    def test_example_2(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
        result = self.solution.reorderList(head)
        self.assertEqual(result.val, 1)
        self.assertEqual(result.next.val, 4)
        self.assertEqual(result.next.next.val, 2)

if __name__ == "__main__":
    unittest.main()

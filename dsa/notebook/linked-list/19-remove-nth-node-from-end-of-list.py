"""
19. Remove Nth Node From End of List (Medium)

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]
"""

import unittest

"""
Approach:
We will use the two-pointer technique. First, move the fast pointer n steps ahead.
Then, move both the fast and slow pointers until the fast pointer reaches the end of the list.
At this point, the slow pointer will be pointing to the node just before the one to be removed.
"""

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        pass

class TestRemoveNthNode(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        result = self.solution.removeNthFromEnd(head, 2)
        self.assertEqual(result.val, 1)
        self.assertEqual(result.next.val, 2)
        self.assertEqual(result.next.next.val, 3)
        self.assertEqual(result.next.next.next.val, 5)

    def test_example_2(self):
        head = ListNode(1)
        result = self.solution.removeNthFromEnd(head, 1)
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()

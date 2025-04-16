"""
206. Reverse Linked List (Easy)

Given the head of a singly linked list, reverse the list and return its head.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []
"""

import unittest

"""
Approach:
We will use an iterative approach to reverse the linked list. We will maintain three pointers: 
prev, curr, and next. We iterate through the list, updating the pointers until the list is reversed.
"""

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pass

class TestReverseLinkedList(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        result = self.solution.reverseList(head)
        self.assertEqual(result.val, 5)
        self.assertEqual(result.next.val, 4)

    def test_example_2(self):
        head = ListNode(1, ListNode(2))
        result = self.solution.reverseList(head)
        self.assertEqual(result.val, 2)
        self.assertEqual(result.next.val, 1)

if __name__ == "__main__":
    unittest.main()

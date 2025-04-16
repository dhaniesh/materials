"""
141. Linked List Cycle (Easy)

Given a linked list, determine if it has a cycle in it.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
"""

import unittest

"""
Approach:
We can use the slow and fast pointer technique. The slow pointer moves one step at a time,
while the fast pointer moves two steps at a time. If they meet, there is a cycle. If the fast pointer 
reaches the end of the list, there is no cycle.
"""

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        pass

class TestLinkedListCycle(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        head = ListNode(3, ListNode(2, ListNode(0, ListNode(-4))))
        head.next.next.next.next = head.next  # create a cycle
        result = self.solution.hasCycle(head)
        self.assertTrue(result)

    def test_example_2(self):
        head = ListNode(1, ListNode(2))
        head.next.next = head  # create a cycle
        result = self.solution.hasCycle(head)
        self.assertTrue(result)

    def test_example_3(self):
        head = ListNode(1)
        result = self.solution.hasCycle(head)
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()

"""
142. Linked List Cycle II (Medium)

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list where tail connects to the node index 1.

Example 2:
Input: head = [1,2], pos = 0
Output: tail connects to node index 0

Example 3:
Input: head = [1], pos = -1
Output: no cycle

Note:
- The number of nodes in the list is in the range [0, 10⁴].
- The value of each node in the list is in the range [-10⁶, 10⁶].
- Do not modify the linked list.
"""

import unittest

"""
Approach:
We can use Floyd’s Tortoise and Hare algorithm (slow and fast pointers) to detect the cycle, 
then use a separate pointer to find the starting node of the cycle.
"""

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        pass

class TestLinkedListCycleII(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        head = ListNode(3, ListNode(2, ListNode(0, ListNode(-4))))
        head.next.next.next = head.next  # Create a cycle
        self.assertEqual(self.solution.detectCycle(head), head.next)

    def test_example_2(self):
        head = ListNode(1, ListNode(2))
        head.next.next = head  # Create a cycle
        self.assertEqual(self.solution.detectCycle(head), head)

    def test_no_cycle(self):
        head = ListNode(1)
        self.assertIsNone(self.solution.detectCycle(head))

if __name__ == "__main__":
    unittest.main()

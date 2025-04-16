"""
876. Middle of the Linked List (Easy)

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Example 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node is node 3.

Example 2:
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since there are two middle nodes, we return the second middle node.

Constraints:
- The number of nodes in the list is in the range [1, 100].
"""

import unittest

"""
Approach:
We can use the slow and fast pointer technique. The fast pointer moves twice as fast as the slow pointer, 
so when the fast pointer reaches the end, the slow pointer will be at the middle.
"""

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        pass

class TestMiddleOfTheLinkedList(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        result = self.solution.middleNode(head)
        self.assertEqual(result.val, 3)

    def test_example_2(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
        result = self.solution.middleNode(head)
        self.assertEqual(result.val, 4)

if __name__ == "__main__":
    unittest.main()

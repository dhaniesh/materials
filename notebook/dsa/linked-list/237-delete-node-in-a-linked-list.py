"""
237. Delete Node in a Linked List (Easy)

Write a function to delete a node in a singly linked list. You will not be given access to the head of the list, 
instead you will be given access to the node to be deleted directly.

Example 1:
Input: head = [4,5,1,9], node = 5
Output: [4,1,9]

Example 2:
Input: head = [4,5,1,9], node = 1
Output: [4,5,9]

Note:
- The linked list will have at least one node.
- The value of the node to be deleted will be unique.
"""

import unittest

"""
Approach:
Since we are not given access to the head, we cannot traverse the list. Instead, we copy the value of the next 
node into the current node, and then delete the next node.
"""

class Solution:
    def deleteNode(self, node: ListNode) -> None:
        pass

class TestDeleteNode(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        head = ListNode(4, ListNode(5, ListNode(1, ListNode(9))))
        node = head.next
        self.solution.deleteNode(node)
        self.assertEqual(head.val, 4)
        self.assertEqual(head.next.val, 1)
        self.assertEqual(head.next.next.val, 9)

if __name__ == "__main__":
    unittest.main()

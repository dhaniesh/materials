"""
25. Reverse Nodes in k-Group (Hard)

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list. 
If the number of nodes is not a multiple of k then left nodes in the end should remain as it is.

Example 1:
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]

Example 2:
Input: head = [1,2,3,4,5], k = 1
Output: [1,2,3,4,5]

Example 3:
Input: head = [1], k = 1
Output: [1]
"""

import unittest

"""
Approach:
We will iterate over the linked list in chunks of k nodes. For each chunk, we reverse the nodes. 
Once the next chunk is reached, we link the reversed part to the rest of the list.
"""

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        pass

class TestReverseNodesInKGroup(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        result = self.solution.reverseKGroup(head, 3)
        self.assertEqual(result.val, 3)
        self.assertEqual(result.next.val, 2)
        self.assertEqual(result.next.next.val, 1)

    def test_example_2(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        result = self.solution.reverseKGroup(head, 1)
        self.assertEqual(result.val, 1)
        self.assertEqual(result.next.val, 2)

    def test_example_3(self):
        head = ListNode(1)
        result = self.solution.reverseKGroup(head, 1)
        self.assertEqual(result.val, 1)

if __name__ == "__main__":
    unittest.main()

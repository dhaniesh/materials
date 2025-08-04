"""
61. Rotate List (Medium)

Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]
"""

import unittest

"""
Approach:
We first find the length of the list. Then we connect the last node to the head to form a circular list. 
Finally, we break the circle by moving the pointer to the (length - k % length)th node.
"""

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        pass

class TestRotateList(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        result = self.solution.rotateRight(head, 2)
        self.assertEqual(result.val, 4)
        self.assertEqual(result.next.val, 5)
        self.assertEqual(result.next.next.val, 1)

    def test_example_2(self):
        head = ListNode(0, ListNode(1, ListNode(2)))
        result = self.solution.rotateRight(head, 4)
        self.assertEqual(result.val, 2)
        self.assertEqual(result.next.val, 0)
        self.assertEqual(result.next.next.val, 1)

if __name__ == "__main__":
    unittest.main()

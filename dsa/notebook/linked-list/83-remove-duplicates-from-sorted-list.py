"""
83. Remove Duplicates from Sorted List (Easy)

Given a sorted linked list, delete all duplicates such that each element appears only once.

Example 1:
Input: head = [1,1,2]
Output: [1,2]

Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]
"""

import unittest

"""
Approach:
We will traverse through the list, comparing the current node's value with the next node's value. 
If they are the same, we skip the next node. If they are different, we continue to the next node.
"""

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        pass

class TestRemoveDuplicates(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        head = ListNode(1, ListNode(1, ListNode(2)))
        result = self.solution.deleteDuplicates(head)
        self.assertEqual(result.val, 1)
        self.assertEqual(result.next.val, 2)

    def test_example_2(self):
        head = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
        result = self.solution.deleteDuplicates(head)
        self.assertEqual(result.val, 1)
        self.assertEqual(result.next.val, 2)
        self.assertEqual(result.next.next.val, 3)

if __name__ == "__main__":
    unittest.main()

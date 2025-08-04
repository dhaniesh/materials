"""
328. Odd Even Linked List (Medium)

Given a singly linked list, group all odd nodes together followed by the even nodes. 
Please note here we are talking about the node numbers and not the values.

You should solve it in O(1) space complexity and O(n) time complexity.

Example 1:
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

Example 2:
Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]

Note:
- The length of the list is between 0 and 10⁴.
- The nodes in the list are indexed starting from 1.
"""

import unittest

"""
Approach:
We can divide the list into two parts: one for odd-indexed nodes and one for even-indexed nodes. 
After traversing the list, we can merge both lists.
"""

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        pass

class TestOddEvenLinkedList(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        result = self.solution.oddEvenList(head)
        self.assertEqual(result.val, 1)
        self.assertEqual(result.next.val, 3)
        self.assertEqual(result.next.next.val, 5)

    def test_example_2(self):
        head = ListNode(2, ListNode(1, ListNode(3, ListNode(5, ListNode(6, ListNode(4, ListNode(7)))))))
        result = self.solution.oddEvenList(head)
        self.assertEqual(result.val, 2)
        self.assertEqual(result.next.val, 3)
        self.assertEqual(result.next.next.val, 6)

if __name__ == "__main__":
    unittest.main()

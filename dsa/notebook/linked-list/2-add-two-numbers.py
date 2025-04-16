"""
2. Add Two Numbers (Medium)

You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""

import unittest

"""
Approach:
We will iterate through both linked lists, adding corresponding digits and keeping track of the carry.
If we reach the end of one list before the other, we continue adding from the remaining list, considering the carry.
"""

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        pass

class TestAddTwoNumbers(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        l1 = ListNode(2, ListNode(4, ListNode(3)))
        l2 = ListNode(5, ListNode(6, ListNode(4)))
        result = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(result.val, 7)
        self.assertEqual(result.next.val, 0)
        self.assertEqual(result.next.next.val, 8)

    def test_example_2(self):
        l1 = ListNode(0)
        l2 = ListNode(0)
        result = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(result.val, 0)

if __name__ == "__main__":
    unittest.main()

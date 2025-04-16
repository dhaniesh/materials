"""
160. Intersection of Two Linked Lists (Easy)

Write a program to find the node where two singly linked lists intersect. 
If the two linked lists have no intersection, return null.

Example 1:
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
Output: intersectVal = 8
Explanation: The intersection node's value is 8, and the two linked lists intersect at that node.

Example 2:
Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: intersectVal = 2
Explanation: The intersection node's value is 2, and the two linked lists intersect at that node.

Note:
- The number of nodes in both lists is in the range [0, 10⁴].
- 1 <= listA.length, listB.length <= 1000
- 1 <= Node.val <= 10⁶
"""

import unittest

"""
Approach:
We can traverse both lists simultaneously with two pointers, one for each list. 
Once the pointers reach the end of their respective lists, we restart the pointer at the head of the other list.
We continue this until the pointers meet at the intersection node.
"""

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pass

class TestIntersectionOfTwoLinkedLists(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        headA = ListNode(4, ListNode(1, ListNode(8, ListNode(4, ListNode(5)))))
        headB = ListNode(5, ListNode(0, ListNode(1, ListNode(8, ListNode(4, ListNode(5))))))
        self.assertEqual(self.solution.getIntersectionNode(headA, headB).val, 8)

    def test_example_2(self):
        headA = ListNode(1, ListNode(9, ListNode(1, ListNode(2, ListNode(4)))))
        headB = ListNode(3, ListNode(2, ListNode(4)))
        self.assertEqual(self.solution.getIntersectionNode(headA, headB).val, 2)

    def test_no_intersection(self):
        headA = ListNode(1, ListNode(2))
        headB = ListNode(3, ListNode(4))
        self.assertIsNone(self.solution.getIntersectionNode(headA, headB))

if __name__ == "__main__":
    unittest.main()

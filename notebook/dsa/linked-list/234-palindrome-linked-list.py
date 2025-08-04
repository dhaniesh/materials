"""
234. Palindrome Linked List (Easy)

Given a singly linked list, return true if it is a palindrome.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false

Note:
- The number of nodes in the list is in the range [1, 10⁵].
- The value of each node in the list is in the range [0, 9].
"""

import unittest

"""
Approach:
We can use a slow and fast pointer technique to find the middle of the list, then reverse the second half and 
compare it with the first half.
"""

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        pass

class TestPalindromeLinkedList(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        head = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
        self.assertTrue(self.solution.isPalindrome(head))

    def test_example_2(self):
        head = ListNode(1, ListNode(2))
        self.assertFalse(self.solution.isPalindrome(head))

if __name__ == "__main__":
    unittest.main()

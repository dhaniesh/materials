"""
138. Copy List with Random Pointer (Medium)

A linked list is given where each node contains an additional random pointer, which could point to any node in the list or null. 
Return a deep copy of the list.

Example 1:
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Example 2:
Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
"""

import unittest

"""
Approach:
We will use a hash map to store the mapping between original nodes and their copies. 
Then, we iterate through the original list and use this mapping to connect the copied nodes.
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        pass

class TestCopyListWithRandomPointer(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        head = Node(7)
        head.next = Node(13)
        head.next.next = Node(11)
        head.next.next.next = Node(10)
        head.next.next.next.next = Node(1)
        result = self.solution.copyRandomList(head)
        self.assertEqual(result.val, 7)
        self.assertEqual(result.next.val, 13)

    def test_example_2(self):
        head = Node(1)
        head.next = Node(2)
        result = self.solution.copyRandomList(head)
        self.assertEqual(result.val, 1)
        self.assertEqual(result.next.val, 2)

if __name__ == "__main__":
    unittest.main()

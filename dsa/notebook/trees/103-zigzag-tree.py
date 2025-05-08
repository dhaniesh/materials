"""
103. Binary Tree Zigzag Level Order Traversal

Given the root of a binary tree, return the zigzag level order traversal 
of its nodes' values. (i.e., from left to right, then right to left for 
the next level and alternate between).

Example:
Input: 
    3
   / \
  9  20
     / \
    15  7

Output: [[3],[20,9],[15,7]]

Constraints:
- The number of nodes in the tree is in the range [0, 2000]
- -100 <= Node.val <= 100
"""

from typing import List, Optional
import unittest
from collections import deque

# Tree node definition
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Zigzag level order traversal solution
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        queue = deque([root])
        left_to_right = True

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if not left_to_right:
                level.reverse()
            result.append(level)
            left_to_right = not left_to_right
        
        return result

# Test suite using unittest
class TestZigzagLevelOrder(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def listToTree(self, arr):
        if not arr:
            return None
        nodes = [TreeNode(val) if val is not None else None for val in arr]
        children = nodes[::-1]
        root = children.pop()
        for node in nodes:
            if node:
                if children:
                    node.left = children.pop()
                if children:
                    node.right = children.pop()
        return root

    def test_example_1(self):
        root = self.listToTree([3, 9, 20, None, None, 15, 7])
        expected = [[3], [20, 9], [15, 7]]
        self.assertEqual(self.solution.zigzagLevelOrder(root), expected)

    def test_empty_tree(self):
        root = self.listToTree([])
        self.assertEqual(self.solution.zigzagLevelOrder(root), [])

    def test_single_node(self):
        root = self.listToTree([1])
        self.assertEqual(self.solution.zigzagLevelOrder(root), [[1]])

    def test_two_levels(self):
        root = self.listToTree([1, 2, 3])
        self.assertEqual(self.solution.zigzagLevelOrder(root), [[1], [3, 2]])

    def test_unbalanced_tree(self):
        root = self.listToTree([1, 2, None, 3])
        self.assertEqual(self.solution.zigzagLevelOrder(root), [[1], [2], [3]])

if __name__ == "__main__":
    unittest.main()

"""
155. Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:
- MinStack() initializes the stack object.
- void push(int val) pushes the element val onto the stack.
- void pop() removes the element on the top of the stack.
- int top() gets the top element of the stack.
- int getMin() retrieves the minimum element in the stack.

Example:
    Input:
        ["MinStack","push","push","push","getMin","pop","top","getMin"]
        [[],[-2],[0],[-3],[],[],[],[]]
    Output:
        [null,null,null,null,-3,null,0,-2]
    Explanation:
        MinStack minStack = new MinStack();
        minStack.push(-2);
        minStack.push(0);
        minStack.push(-3);
        minStack.getMin(); --> Returns -3
        minStack.pop();
        minStack.top();    --> Returns 0
        minStack.getMin(); --> Returns -2

Constraints:
    - -2^31 <= val <= 2^31 - 1
    - Methods pop(), top(), and getMin() operations will always be called on non-empty stacks.
    - At most 3 * 10^4 calls will be made to push, pop, top, and getMin.
"""

import unittest


class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if self.min_stack and self.min_stack[-1] == val:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


class TestMinStack(unittest.TestCase):

    def test_basic_operations(self):
        s = MinStack()
        s.push(-2)
        s.push(0)
        s.push(-3)
        self.assertEqual(s.getMin(), -3)
        s.pop()
        self.assertEqual(s.top(), 0)
        self.assertEqual(s.getMin(), -2)

    def test_increasing_values(self):
        s = MinStack()
        for val in [1, 2, 3, 4, 5]:
            s.push(val)
        self.assertEqual(s.getMin(), 1)
        s.pop()
        self.assertEqual(s.top(), 4)
        self.assertEqual(s.getMin(), 1)

    def test_decreasing_values(self):
        s = MinStack()
        for val in [5, 4, 3, 2, 1]:
            s.push(val)
        self.assertEqual(s.getMin(), 1)
        s.pop()
        self.assertEqual(s.getMin(), 2)
        s.pop()
        self.assertEqual(s.getMin(), 3)

    def test_duplicate_minimums(self):
        s = MinStack()
        s.push(2)
        s.push(2)
        s.push(3)
        self.assertEqual(s.getMin(), 2)
        s.pop()
        s.pop()
        self.assertEqual(s.getMin(), 2)

    def test_single_element(self):
        s = MinStack()
        s.push(42)
        self.assertEqual(s.top(), 42)
        self.assertEqual(s.getMin(), 42)
        s.pop()
        self.assertEqual(s.stack, [])
        self.assertEqual(s.min_stack, [])


if __name__ == "__main__":
    unittest.main()

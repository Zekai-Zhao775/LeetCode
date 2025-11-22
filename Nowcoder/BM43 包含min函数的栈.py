# -*- coding:utf-8 -*-
class Solution:
    # use a min heap to keep track of min?
    # extra O(n) space, but will not be O(n), since heapify will cost O(n) each time(or push to heap cost O(logn) for new element)
    # no min heap here

    # how to use extra space to solve this
    # use another stack to track min for a state of the current stack
    # since after pop the element the stack will go back to original state
    # then the min is still the original one

    # like a state machine


    def __init__(self) -> None:
        self.stack = []
        self.min_stack = []

    def push(self, node):
        # write code here
        self.stack.append(node)
        if len(self.min_stack) == 0 or node <= self.min_stack[-1]:
            self.min_stack.append(node)

    def pop(self):
        # write code here
        num = self.stack.pop()
        if num == self.min_stack[-1]:
            self.min_stack.pop()
        return num

    def top(self):
        # write code here
        return self.stack[-1]

    def min(self):
        # write code here
        return self.min_stack[-1]
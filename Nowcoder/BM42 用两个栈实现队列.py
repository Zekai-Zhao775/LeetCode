# -*- coding:utf-8 -*-
class Solution:
    # to make it space O(n), we can't just use two index with a list, then it grows overtime
    # but delete from head of a list will be O(n)
    # so when deleting only delete from tail of a list?
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, node):
        # write code here
        # push to tail of queue
        self.stack1.append(node)
    def pop(self):
        # pop form head of queue
        if len(self.stack2) != 0:
            return self.stack2.pop()
        elif len(self.stack2) == 0:
            # move stack1 to stack2
            # lazy delete, all element move exactly once, so still O(1)
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()
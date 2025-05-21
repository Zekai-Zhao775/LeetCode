from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        sum_max = -10 ** 5 - 1
        level_max = 0
        if not root:
            return

        queue = deque()
        queue.append(root)
        level = 0

        while queue:
            level_size = len(queue)
            i = 0
            sum_level = 0
            level += 1
            for i in range(level_size):
                node = queue.popleft()
                sum_level += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if sum_level > sum_max:
                sum_max = sum_level
                level_max = level

        return level_max
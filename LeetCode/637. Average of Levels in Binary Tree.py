# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, List


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # deque to store node
        # [] to store result

        nodes = deque()
        nodes.append((root, 0))
        level_curr = 0
        sum_curr = 0
        count_curr = 0
        result = []
        while nodes:
            node, level = nodes.popleft()
            if node.left:
                nodes.append((node.left, level + 1))
            if node.right:
                nodes.append((node.right, level + 1))

            if level == level_curr:
                sum_curr += node.val
                count_curr += 1
            elif level != level_curr:
                result.append(sum_curr / count_curr)
                level_curr += 1
                sum_curr = node.val
                count_curr = 1

        if count_curr != 0:
            result.append(sum_curr / count_curr)

        return result
# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, List


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque()
        q.append((root, 0))

        level_curr = 0
        nodes_curr = []
        result = []

        while q:
            node, level = q.popleft()
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))

            if level == level_curr:
                nodes_curr.append(node.val)
            elif level != level_curr:
                result.append(nodes_curr)
                nodes_curr = [node.val]
                level_curr += 1

        if nodes_curr != []:
            result.append(nodes_curr)

        return result
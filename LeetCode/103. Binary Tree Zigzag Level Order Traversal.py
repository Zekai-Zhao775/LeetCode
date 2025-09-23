# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, List


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # do normal travesal
        # reverse half of it

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

        for i in range(len(result)):
            if i % 2 == 1:
                result[i].reverse()

        return result
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # preorder, root-left-right
        # preorder dfs to store every node in a list
        # give them value
        nodes = []
        if not root:
            return root

        def dfs(node):
            if not node:
                return
            nodes.append(node)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        if len(nodes) == 1:
            return root
        i = 0
        while i < len(nodes) - 1:
            nodes[i].left = None
            nodes[i].right = nodes[i + 1]
            i += 1
        nodes[i].left = None
        nodes[i].right = None

        return root
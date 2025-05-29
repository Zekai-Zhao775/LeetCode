# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def dfs(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if not node:
                return None

            if node.val == val:
                return node

            if val > node.val:
                return dfs(node.right)

            if val < node.val:
                return dfs(node.left)

        return dfs(root)

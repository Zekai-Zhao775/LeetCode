# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # in order traverse
        self.idx = 1
        self.kth = -1
        def dfs(node):
            if not node:
                return
            else:
                dfs(node.left)
                if self.kth != -1:
                    return
                if self.idx == k:
                    self.kth = node.val
                    return
                else:
                    self.idx += 1
                dfs(node.right)
        dfs(root)
        return self.kth
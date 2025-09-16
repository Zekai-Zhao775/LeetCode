# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.result = 0

        def dfs(node, num):
            if not node:
                return
            num = num * 10 + node.val
            if node.left == None and node.right == None:
                self.result += num
            dfs(node.left, num)
            dfs(node.right, num)

        dfs(root, 0)
        return self.result
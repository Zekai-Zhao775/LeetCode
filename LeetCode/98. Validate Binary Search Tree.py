# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # in order traverse
        self.last = - 2 ** 31 - 1
        def dfs(node):
            if not node:
                return True
            else:
                left = dfs(node.left)
                if node.val <= self.last:
                    middle = False
                else:
                    self.last = node.val
                    middle = True
                right = dfs(node.right)
                return left and middle and right
        return dfs(root)
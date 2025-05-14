# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        # O(n*n) Time Limit Exceeded

        # 0 left 1 right
        def ZigZag(root: Optional[TreeNode], direction: int) -> int:
            if root == None:
                return 0
            elif direction == 0:
                if root.left == None:
                    return 0
                else:
                    return 1 + ZigZag(root.left, 1)
            elif direction == 1:
                if root.right == None:
                    return 0
                else:
                    return 1 + ZigZag(root.right, 0)

        if root == None:
            return 0
        else:
            return max(ZigZag(root, 0), ZigZag(root, 1), self.longestZigZag(root.left), self.longestZigZag(root.right))
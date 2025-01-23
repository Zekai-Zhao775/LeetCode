# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# class Solution:
#     def minDepth(self, root: Optional[TreeNode]) -> int:
#         if root == None:
#             return 0
#         elif self.minDepth(root.left) == 0: # No need to traversal here, if not 0 will cause time problem
#             return 1 + self.minDepth(root.right)
#         elif self.minDepth(root.right) == 0:
#             return 1 + self.minDepth(root.left)
#         else:
#             return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        elif root.left == None:
            return 1 + self.minDepth(root.right)
        elif root.right == None:
            return 1 + self.minDepth(root.left)
        else:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if root == None:
#             return 0
#         if root.left == None and root.right == None:
#             return 1
#         elif root.left == None and root.right != None:
#             return 1 + self.maxDepth(root.right)
#         elif root.left != None and root.right == None:
#             return 1 + self.maxDepth(root.left)
#         else:
#             return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
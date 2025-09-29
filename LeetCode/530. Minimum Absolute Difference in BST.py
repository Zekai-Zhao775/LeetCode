# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # in order
        self.last = -1
        self.mad = 10 ** 5
        self.diff = 0
        def dfs(node):
            if not node:
                return
            else:
                dfs(node.left)
                if self.last == -1:
                    self.last = node.val
                else:
                    self.diff = node.val - self.last
                    if self.diff < self.mad:
                        self.mad = self.diff
                    self.last = node.val
                dfs(node.right)
        dfs(root)
        return self.mad

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
#         # in order
#         vals = []
#         def dfs(node):
#             if not node:
#                 return
#             else:
#                 dfs(node.left)
#                 vals.append(node.val)
#                 dfs(node.right)
#         dfs(root)
#         mad = 10 ** 5
#         diff = 0
#         i = 1
#         while i < len(vals):
#             diff = vals[i] - vals[i - 1]
#             if diff < mad:
#                 mad = diff
#             i += 1
#         return mad
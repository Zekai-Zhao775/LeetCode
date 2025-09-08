# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return root
        if root.left:
            root.left = self.invertTree(root.left)
        if root.right:
            root.right = self.invertTree(root.right)
        node_temp = root.left
        root.left = root.right
        root.right = node_temp
        return root

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root != None:
            temp = root.left
            root.left = root.right
            root.right = temp
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root
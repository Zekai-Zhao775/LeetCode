# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # if self.dfsLeaf(root1) == self.dfsLeaf(root2):
        #     return True
        # else:
        #     return False
        return self.dfsLeaf(root1) == self.dfsLeaf(root2)

    def dfsLeaf(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        elif root.left == None and root.right == None:
            return [root.val]
        else:
            return self.dfsLeaf(root.left) + self.dfsLeaf(root.right)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfsSum(root: Optional[TreeNode], lastSum: int) -> bool:
            if root == None:
                return False
            elif root.left == None and root.right == None:
                lastSum += root.val
                if lastSum == targetSum:
                    return True
                else:
                    return False
            else:
                lastSum += root.val
                return dfsSum(root.left, lastSum) or dfsSum(root.right, lastSum)

        return dfsSum(root, 0)

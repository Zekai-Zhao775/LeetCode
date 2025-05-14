# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # for every node in the tree
        # check the targetsum(that starts with current root, so no repeat)
        # O(n*n)

        def pathSumRoot(root: Optional[TreeNode], lastSum: int) -> int:
            if root == None:
                return 0
            elif root.left == None and root.right == None:
                lastSum += root.val
                if lastSum == targetSum:
                    return 1
                else:
                    return 0
            else:
                lastSum += root.val
                if lastSum == targetSum:
                    return 1 + pathSumRoot(root.left, lastSum) + pathSumRoot(root.right, lastSum)
                else:
                    return 0 + pathSumRoot(root.left, lastSum) + pathSumRoot(root.right, lastSum)

        if root == None:
            return 0
        else:
            return pathSumRoot(root, 0) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)


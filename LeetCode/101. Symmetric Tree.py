# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True

        def isMirror(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            if left == None and right == None:
                return True
            elif left == None or right == None:
                return False
            elif left.val != right.val:
                return False
            else:
                return isMirror(left.right, right.left) and isMirror(left.left, right.right)

        return isMirror(root.left, root.right)

        # ❌ Wrong: added "self" here
        # This makes Python think isMirror needs THREE args (self, left, right)
        # But when we call it below, we only pass TWO (root.left, root.right).
        # That's why we get:
        # TypeError: isMirror() missing 1 required positional argument: 'right'
        # def isMirror(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        #     if left == None and right == None:
        #         return True
        #     elif left == None or right == None:
        #         return False
        #     # ❌ Wrong again: using self.isMirror(...)
        #     # "self" here refers to the Solution instance, but isMirror is just
        #     # a nested function, not a method of Solution.
        #     else:
        #         return self.isMirror(left.right, right.left) and self.isMirror(left.left, right.right)

        # ❌ At this call, we pass only 2 args, but function signature requires 3.
        # return isMirror(root.left, root.right)





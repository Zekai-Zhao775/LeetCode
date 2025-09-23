# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # get root from postorder[-1]
        # then left and right from inorder
        # recurse

        # edge case
        if len(postorder) == 0:
            return None
        elif len(postorder) == 1:
            return TreeNode(postorder[0])
        else:
            root = TreeNode(postorder[-1])
            root_i_in = inorder.index(root.val)
            root.left = self.buildTree(inorder[0:root_i_in], postorder[0:root_i_in])
            root.right = self.buildTree(inorder[root_i_in + 1:], postorder[root_i_in:len(postorder) - 1])
            return root
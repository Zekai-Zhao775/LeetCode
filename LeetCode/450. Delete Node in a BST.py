# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # key == root.val
            if not root.left and not root.right:
                return None
            elif not root.left and root.right:
                return root.right
            elif root.left and not root.right:
                return root.left
            else:
                # find the min from right subtree
                # replace the root val with min val
                # delete the min from right subtree
                current = root.right
                while current.left:
                    current = current.left
                root.val = current.val
                root.right = self.deleteNode(root.right, current.val)
        return root


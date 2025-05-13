# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        max = root.val
        return 1 + self.goodNodesDFS(root.left, max) + self.goodNodesDFS(root.right, max)

    def goodNodesDFS(self, root: TreeNode, max: int) -> int:
        if root == None:
            return 0
        if root.val >= max:
            max = root.val
            return 1 + self.goodNodesDFS(root.left, max) + self.goodNodesDFS(root.right, max)
        else:
            return self.goodNodesDFS(root.left, max) + self.goodNodesDFS(root.right, max)

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.nodes = []

        # iterate at first when init
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            self.nodes.append(node)
            dfs(node.right)

        dfs(self.root)
        self.curr = 0

    def next(self) -> int:
        val = self.nodes[self.curr].val
        self.curr += 1
        return val

    def hasNext(self) -> bool:
        if self.curr >= len(self.nodes):
            return False
        else:
            return True

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
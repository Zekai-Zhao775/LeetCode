from functools import lru_cache
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# O(n*n) Time Limit Exceeded
# class Solution:
#     def longestZigZag(self, root: Optional[TreeNode]) -> int:
#         # 0 left 1 right
#         def ZigZag(root: Optional[TreeNode], direction: int) -> int:
#             if root == None:
#                 return 0
#             elif direction == 0:
#                 if root.left == None:
#                     return 0
#                 else:
#                     return 1 + ZigZag(root.left, 1)
#             elif direction == 1:
#                 if root.right == None:
#                     return 0
#                 else:
#                     return 1 + ZigZag(root.right, 0)

#         if root == None:
#             return 0
#         else:
#             return max(ZigZag(root, 0), ZigZag(root, 1), self.longestZigZag(root.left), self.longestZigZag(root.right))

# O(n) Time
# O(n) Space
# @lru_cache(maxsize=None)
# def ZigZag(node: Optional["TreeNode"], direction: int) -> int:
#     # 0 → go left next, 1 → go right next
#     if node is None:
#         return 0
#     if direction == 0:
#         return 0 if node.left  is None else 1 + ZigZag(node.left,  1)
#     else:
#         return 0 if node.right is None else 1 + ZigZag(node.right, 0)

# class Solution:
#     def longestZigZag(self, root: Optional["TreeNode"]) -> int:
#         if root is None:
#             return 0
#         return max(
#             ZigZag(root, 0),
#             ZigZag(root, 1),
#             self.longestZigZag(root.left),
#             self.longestZigZag(root.right),
#         )


class Solution:
    def __init__(self):
        # one shared cache for the whole recursion
        self.memo = {}  # key = (id(node), direction) → length

    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        # 0 = last move was right → must go left next
        # 1 = last move was left  → must go right next
        def ZigZag(node: Optional[TreeNode], direction: int) -> int:
            if node is None:
                return 0

            key = (id(node), direction)
            if key in self.memo:  # ← plain-dict memoisation
                return self.memo[key]

            if direction == 0:
                ans = 0 if node.left is None else 1 + ZigZag(node.left, 1)
            else:
                ans = 0 if node.right is None else 1 + ZigZag(node.right, 0)

            self.memo[key] = ans
            return ans

        if root is None:
            return 0
        return max(
            ZigZag(root, 0),
            ZigZag(root, 1),
            self.longestZigZag(root.left),
            self.longestZigZag(root.right),
        )
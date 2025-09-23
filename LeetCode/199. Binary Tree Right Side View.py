from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque()
        q.append((root, 0))
        result = []
        level_curr = 0
        num_curr = -101

        while q:
            node, level = q.popleft()
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))
            if level == level_curr:
                num_curr = node.val
            elif level != level_curr:
                result.append(num_curr)
                level_curr += 1
                num_curr = node.val

        if num_curr != -101:
            result.append(num_curr)

        return result

# level-order BFS
# class Solution:
#     def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
#         result = []
#
#         def bfsLevel():
#             if not root:
#                 return
#             queue = deque()
#             queue.append(root)
#
#             while queue:
#                 level_size = len(queue)
#                 i = 0
#                 for i in range(level_size):
#                     node = queue.popleft()
#                     print(node.val)
#                     if i == level_size - 1:
#                         result.append(node.val)
#                     if node.left:
#                         queue.append(node.left)
#                     if node.right:
#                         queue.append(node.right)
#
#         bfsLevel()
#         return result

# Wrong Answer 213 / 217 testcases passed
# class Solution:
#     def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
#         result = []

#         def bfs():
#             # queue = deque([root])
#             if not root:
#                 return
#             queue = deque()
#             queue.append([root, 1])
#             node = queue.popleft()
#             print(node[0].val)
#             result.append(node[0].val)

#             if node[0].left:
#                 if not node[0].right:
#                     queue.append([node[0].left, 1])
#                 else:
#                     queue.append([node[0].left, 0])
#             if node[0].right:
#                 queue.append([node[0].right, 1])

#             while queue:
#                 node = queue.popleft()
#                 print(node[0].val)
#                 if node[1] == 1:
#                     result.append(node[0].val)
#                 elif node[1] == 0 and not queue:
#                     result.append(node[0].val)

#                 if node[0].left:
#                     if not node[0].right:
#                         queue.append([node[0].left, node[1]])
#                     else:
#                         queue.append([node[0].left, 0])
#                 if node[0].right:
#                     queue.append([node[0].right, node[1]])
#         bfs()
#         return result
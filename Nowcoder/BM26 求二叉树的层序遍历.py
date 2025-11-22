from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param root TreeNode类
# @return int整型二维数组
#
from collections import deque

class Solution:
    def levelOrder(self , root: TreeNode) -> List[List[int]]:
        # write code here

        # edge case
        if not root:
            return []

        # bfs, queue to store
        # also need to track which level
        result = []
        queue = deque()
        queue.append((root, 0))
        visited = set()

        while queue:
            node, level = queue.popleft()
            if level not in visited:
                visited.add(level)
                result.append([])
            result[level].append(node.val)
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        return result
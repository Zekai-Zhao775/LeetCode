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
# @return int整型一维数组
#
class Solution:
    def preorderTraversal(self , root: TreeNode) -> List[int]:
        # write code here
        result = []
        def dfs_preorder(node):
            if not node:
                return
            else:
                result.append(node.val)
                dfs_preorder(node.left)
                dfs_preorder(node.right)
        dfs_preorder(root)
        return result
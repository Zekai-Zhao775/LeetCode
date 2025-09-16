# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # add a pointer to parent node?
        # then O(n) sacn, O(logn) find LCA, O(n) space
        # use a {} to store this
        # a bit too complicate

        # dfs 2 times
        # record the path
        # return min path[-1]
        # O(2n)

        def dfs(node, target, path):
            if not node:
                return False
            path.append(node)
            if node == target:
                return True
            if dfs(node.left, target, path) or dfs(node.right, target, path):
                return True
            path.pop()
            return False

        path_p, path_q = [], []
        dfs(root, p, path_p)
        dfs(root, q, path_q)

        LCA = None
        for i in range(min(len(path_p), len(path_q))):
            if path_p[i] == path_q[i]:
                LCA = path_p[i]
            else:
                break

        return LCA
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def allAncestor(root: 'TreeNode', target: 'TreeNode') -> list['TreeNode']:
            def dfs(current: 'TreeNode') -> list['TreeNode']:
                if current == None:
                    return []
                elif current == target:
                    return [current]
                else:
                    currentLeft = dfs(current.left)
                    if target in currentLeft:
                        return [current] + currentLeft
                    else:
                        currentRight = dfs(current.right)
                        if target in currentRight:
                            return [current] + currentRight
                        return []
                # elif target in [current] + dfs(current.left):
                #     return [current] + dfs(current.left)
                # elif target in [current] + dfs(current.right):
                #     return [current] + dfs(current.right)
                # else:
                #     return []

            return dfs(root)

        # for node in allAncestor(root, p):
        #     print(node.val)
        # print("---------")
        # for node in allAncestor(root, q):
        #     print(node.val)

        # pAncestor = allAncestor(root, p)
        # qAncestor = allAncestor(root, q)
        # i = len(pAncestor) - 1
        # while i >= 0:
        #     if pAncestor[i] in qAncestor:
        #         return pAncestor[i]
        #     i -= 1
        pAncestor = allAncestor(root, p)  # O(n)
        qAncestor = set(allAncestor(root, q))  # O(n) to build + O(1) lookups
        for node in reversed(pAncestor):  # up to O(n) iterations
            if node in qAncestor:  # O(1) each
                return node

        return None
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # use [][] to store each layer
        # dfs with depth var
        store = [[] for i in range(6000)]

        def dfs(node, depth):
            if not node:
                return
            store[depth].append(node)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)

        for i in range(len(store)):
            if len(store[i]) == 0:
                break
            else:
                j = 0
                while j < len(store[i]) - 1:
                    store[i][j].next = store[i][j + 1]
                    j += 1
                store[i][j].next = None

        return root
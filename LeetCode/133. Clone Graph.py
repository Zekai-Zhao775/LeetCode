# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # use to dict to map node to newNode
        # this will function as a visited for first iteration too
        # (if key in dict, then visited)
        # iterate once to create all newNode (without neighbors)
        if not node:
            return None
        node_map = {}
        def dfs(node):
            if node in node_map:
                return
            else:
                newNode = Node(node.val)
                node_map[node] = newNode
                for n in node.neighbors:
                    dfs(n)
                return
        dfs(node)

        visited = set()
        def dfs_connect(node):
            if node in visited:
                return
            else:
                visited.add(node)
                for n in node.neighbors:
                    node_map[node].neighbors.append(node_map[n])
                for n in node.neighbors:
                    dfs_connect(n)
                return
        dfs_connect(node)

        return node_map[node]
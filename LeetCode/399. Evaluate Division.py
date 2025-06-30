import string
from collections import defaultdict, deque
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Create a hashmap to store the graph
        # a -> [b, a/b]
        adj = defaultdict(list)
        for i, equation in enumerate(equations):
            a, b = equation
            adj[a].append([b, values[i]])
            adj[b].append([a, 1 / values[i]])

        def bfs(start, end):
            if start not in adj or end not in adj:
                return -1.0
            queue = deque()
            visited = set()

            queue.append([start, 1.0])
            visited.add(start)

            while queue:
                n, w = queue.popleft()
                if n == end:
                    return w
                for nn, ww in adj[n]:
                    if nn not in visited:
                        queue.append([nn, w * ww])
                        visited.add(nn)
            return -1.0

        result = []
        for q in queries:
            result.append(bfs(q[0], q[1]))
        return result

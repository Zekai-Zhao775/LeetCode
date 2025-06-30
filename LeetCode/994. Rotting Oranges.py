from collections import defaultdict, deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # all rotten orange doing bfs at the same time, sharing same visited
        # if still orange not in visited, return -1
        # otherwise return steps

        m = len(grid)
        n = len(grid[0])
        rotten_oranges = set()
        count_orange = 0

        def is_orange(cell: tuple):
            if cell[0] >= 0 and cell[0] < m and cell[1] >= 0 and cell[1] < n:
                if grid[cell[0]][cell[1]] != 0:
                    return True
            else:
                return False

        # build graph with adj, (x, y) the tuple as key
        adj = defaultdict(list)
        i, j = 0, 0
        while i < m:
            j = 0
            while j < n:
                if grid[i][j] != 0:
                    count_orange += 1
                    if grid[i][j] == 2:
                        rotten_oranges.add((i, j))
                    neighbors = []
                    # left up right down
                    neighbors.append((i, j - 1))
                    neighbors.append((i + 1, j))
                    neighbors.append((i, j + 1))
                    neighbors.append((i - 1, j))
                    for neighbor in neighbors:
                        if is_orange(neighbor):
                            adj[(i, j)].append(neighbor)
                j += 1
            i += 1

        # bfs all rotten orange at the same time (add them to the queue at first)
        visited = set()
        queue = deque()
        minutes = 0
        for orange in rotten_oranges:
            visited.add(orange)
            queue.append([orange, 0])

        while queue:
            orange, minutes = queue.popleft()
            for neighbor in adj[orange]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append([neighbor, minutes + 1])
        print(visited)
        print(count_orange)
        if len(visited) != count_orange:
            return -1
        else:
            return minutes


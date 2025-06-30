from collections import deque
from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # find shortest, use bfs
        m = len(maze)
        n = len(maze[0])

        def isNotWallAndInMaze(cell: List[int]):
            if (cell[0] >= 0 and cell[0] < m) and (cell[1] >= 0 and cell[1] < n):
                if maze[cell[0]][cell[1]] == ".":
                    return True
            else:
                return False

        def isExit(cell: List[int]):
            if cell == entrance:
                return False
            if (cell[0] == 0 or cell[0] == (m - 1)) or (cell[1] == 0 or cell[1] == (n - 1)):
                if maze[cell[0]][cell[1]] == ".":
                    return True
            else:
                return False

        visited = set()
        queue = deque()
        steps = 0

        queue.append([entrance, steps])
        visited.add((entrance[0], entrance[1]))

        while queue:
            v, steps = queue.popleft()
            if isExit(v):
                return steps
            # left->up->right->down
            neighbors = []
            neighbors.append([v[0], v[1] - 1])
            neighbors.append([v[0] - 1, v[1]])
            neighbors.append([v[0], v[1] + 1])
            neighbors.append([v[0] + 1, v[1]])

            for neighbor in neighbors:
                if ((neighbor[0], neighbor[1]) not in visited) and isNotWallAndInMaze(neighbor):
                    queue.append([neighbor, steps + 1])
                    visited.add((neighbor[0], neighbor[1]))

        return -1
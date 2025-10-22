from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # build adj list from matrix
        # iterate unvisited node that is '1', the times we can do a whole iterate is the number of islands
        # use dfs or bfs, both fine, time O(m*n), space O(m*n)
        # or just dfs the matrix directly
        # mark the visted as "0" so we don't have to visit again
        # each time we visit "1", count++
        m = len(grid)
        n = len(grid[0])

        def dfs(x, y):
            grid[x][y] = '0'
            neighbor = []
            if x - 1 >= 0 and grid[x - 1][y] == '1':
                dfs(x - 1, y)
            if x + 1 < m and grid[x + 1][y] == '1':
                dfs(x + 1, y)
            if y - 1 >= 0 and grid[x][y - 1] == '1':
                dfs(x, y - 1)
            if y + 1 < n and grid[x][y + 1] == '1':
                dfs(x, y + 1)
            return

        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)

        return count
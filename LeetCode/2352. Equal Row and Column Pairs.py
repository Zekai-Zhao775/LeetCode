from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # Rotate the matrix 90 degrees counterclockwise O(n*n)
        n = len(grid)
        gridNew = []
        row = []
        i = 0
        j = 0
        while j < n:
            row = []
            i = 0
            while i < n:
                row.append(grid[i][j])
                i += 1
            gridNew.append(row)
            j += 1

        # two dict to store row and column
        row1 = {}
        row2 = {}

        for row in grid:
            key = tuple(row)
            if key not in row1:
                row1[key] = 1
            else:
                row1[key] += 1
        for row in gridNew:
            key = tuple(row)
            if key not in row2:
                row2[key] = 1
            else:
                row2[key] += 1
        # print(grid)
        # print(gridNew)
        # print(row1)
        # print(row2)
        count = 0
        for key in row1:
            if key in row2:
                count += row1[key] * row2[key]
        return count
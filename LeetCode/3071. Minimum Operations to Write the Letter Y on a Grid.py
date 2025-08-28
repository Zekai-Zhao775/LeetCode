from typing import List


class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        # use dict to store y and non y
        n = len(grid)
        y = {}
        y[0] = 0
        y[1] = 0
        y[2] = 0
        y_count = 0
        y_non = {}
        y_non[0] = 0
        y_non[1] = 0
        y_non[2] = 0
        y_non_count = 0
        for i in range(n):
            for j in range(n):
                if (i == j and i <= n // 2) or (i == n - j - 1 and i <= n // 2) or (i >= n // 2 and j == n // 2):
                    y[grid[i][j]] += 1
                    y_count += 1
                else:
                    y_non[grid[i][j]] += 1
                    y_non_count += 1
        operations = 0
        operations_min = n * n
        for i in range(3):
            for j in range(3):
                if i != j:
                    operations = y_count - y[i] + y_non_count - y_non[j]
                    if operations < operations_min:
                        operations_min = operations
        return operations_min
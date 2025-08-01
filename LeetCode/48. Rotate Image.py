from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # (i, j) -> (j, n - i - 1) ->(n - i - 1, n - j - 1)->(n - j - 1, i)->(i, j)
        # n = len(matrix)
        i, j = 0, 0
        n = len(matrix)
        while i < len(matrix) // 2:
            j = i
            while j - i < len(matrix) - 1 - i * 2:
                num_temp = matrix[n - j - 1][i]
                matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
                matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
                matrix[j][n - i - 1] = matrix[i][j]
                matrix[i][j] = num_temp
                j += 1
            i += 1
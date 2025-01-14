from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        i = 0
        j = 0
        # m, n
        m = len(matrix)
        n = len(matrix[0])
        m_0 = []
        n_0 = []

        i = 0
        j = 0

        while i < m:
            j = 0
            while j < n:
                if matrix[i][j] == 0:
                    m_0.append(i)
                    n_0.append(j)
                j += 1
            i += 1

        i = 0
        j = 0

        while i < m:
            j = 0
            while j < n:
                if i in m_0 or j in n_0:
                    matrix[i][j] = 0
                j += 1
            i += 1
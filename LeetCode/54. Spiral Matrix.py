from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # edge case
        result = []
        m = len(matrix)
        n = len(matrix[0])
        if m == 1:
            return matrix[0]
        if n == 1:
            for l in matrix:
                result.append(l[0])
            return result
        max_right = n - 1
        max_left = 0
        max_top = 1
        max_bottom = m - 1
        # 1, right, 2 down, 3 left, 4 up
        state = 1
        i, j = 0, 0
        count = 0
        while count < m * n:
            result.append(matrix[i][j])
            if state == 1:
                j += 1
                if j == max_right:
                    max_right -= 1
                    state = 2
            elif state == 2:
                i += 1
                if i == max_bottom:
                    max_bottom -= 1
                    state = 3
            elif state == 3:
                j -= 1
                if j == max_left:
                    max_left += 1
                    state = 4
            elif state == 4:
                i -= 1
                if i == max_top:
                    max_top += 1
                    state = 1
            count += 1
        return result
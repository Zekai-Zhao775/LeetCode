from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # simple binary search, but need to pay attention updating the left, right, mid
        m = len(matrix)
        n = len(matrix[0])

        # edge case
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        if target == matrix[0][0] or target == matrix[-1][-1]:
            return True

        # still use 0 --- m*n-1 represents the left, right, mid, but convert to x,y everytime use it
        left = 0
        right = m * n - 1
        mid = 0
        while left <= right:
            mid = (left + right) // 2
            x = mid // n
            y = mid % n
            if target == matrix[x][y]:
                return True
            elif target < matrix[x][y]:
                right = mid - 1
            elif target > matrix[x][y]:
                left = mid + 1
        return False
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param mat int整型二维数组
# @param n int整型
# @return int整型二维数组
#
from typing import List


class Solution:
    def rotateMatrix(self, mat: List[List[int]], n: int) -> List[List[int]]:
        # write code here
        # do rotation starting from 1/4 of the matrix, use a temp O(1) to keep track
        # for odd, rotate the middle part at the end
        # (x, y)->(y, n-x-1)->(n-x-1, n-y-1)->(n-y-1, x)
        for i in range(n // 2):
            for j in range(n // 2):
                last = mat[i][j]
                mat[i][j] = mat[n - j - 1][i]

                temp = mat[j][n - i - 1]
                mat[j][n - i - 1] = last
                last = temp

                temp = mat[n - i - 1][n - j - 1]
                mat[n - i - 1][n - j - 1] = last
                last = temp

                temp = mat[n - j - 1][i]
                mat[n - j - 1][i] = last

        # handle add
        if n % 2 == 1:
            for i in range(n // 2):
                j = n // 2
                last = mat[i][j]
                mat[i][j] = mat[n - j - 1][i]

                temp = mat[j][n - i - 1]
                mat[j][n - i - 1] = last
                last = temp

                temp = mat[n - i - 1][n - j - 1]
                mat[n - i - 1][n - j - 1] = last
                last = temp

                temp = mat[n - j - 1][i]
                mat[n - j - 1][i] = last

        return mat
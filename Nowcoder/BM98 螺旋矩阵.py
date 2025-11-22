#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param matrix int整型二维数组
# @return int整型一维数组
#
from typing import List


class Solution:
    def spiralOrder(self , matrix: List[List[int]]) -> List[int]:
        # write code here
        # edge case
        if len(matrix) == 0:
            return []
        m = len(matrix)
        n = len(matrix[0])
        count = 0
        result = []
        i = 0
        j = 0
        move = 1 # 1 right, 2, down, 3 left, 4 up
        # boundary
        up = 1
        down = m - 1
        left = 0
        right = n - 1
        while count < m*n:
            result.append(matrix[i][j])
            count += 1
            # right
            if move == 1:
                if j + 1 <= right:
                    j += 1
                    continue
                else:
                    # turn down
                    move = 2
                    right -= 1
                    i += 1
                    continue
            # down
            elif move == 2:
                if i + 1 <= down:
                    i += 1
                    continue
                else:
                    # turn left
                    move = 3
                    down -= 1
                    j -= 1
                    continue
            # left
            elif move == 3:
                if j - 1 >= left:
                    j -= 1
                    continue
                else:
                    # turn up
                    move = 4
                    left += 1
                    i -= 1
                    continue
            # up
            elif move == 4:
                if i - 1 >= up:
                    i -= 1
                    continue
                else:
                    # turn right
                    move = 1
                    up += 1
                    j += 1
                    continue
        return result
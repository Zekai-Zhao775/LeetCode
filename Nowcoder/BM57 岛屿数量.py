#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 判断岛屿数量
# @param grid char字符型二维数组
# @return int整型
#
from typing import List


class Solution:
    def solve(self , grid: List[List[str]]) -> int:
        # write code here
        # dfs
        def remove_island(x, y):
            grid[x][y] = '0'
            if x + 1 < len(grid) and grid[x + 1][y] == '1':
                remove_island(x + 1, y)
            if x - 1 >= 0 and grid[x - 1][y] == '1':
                remove_island(x - 1, y)
            if y + 1 < len(grid[0]) and grid[x][y + 1] == '1':
                remove_island(x, y + 1)
            if y - 1 >= 0 and grid[x][y - 1] == '1':
                remove_island(x, y - 1)
            return

        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    remove_island(i, j)
        return count
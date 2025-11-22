#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param numbers int整型一维数组
# @return int整型
#
from typing import List


class Solution:
    def MoreThanHalfNum_Solution(self , numbers: List[int]) -> int:
        # write code here
        n = len(numbers)
        visited = {}
        for num in numbers:
            if num not in visited:
                visited[num] = 1
                if visited[num] > n // 2:
                    return num
            else:
                visited[num] += 1
                if visited[num] > n // 2:
                    return num
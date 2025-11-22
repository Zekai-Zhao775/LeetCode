#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param numbers int整型一维数组
# @param target int整型
# @return int整型一维数组
#
from typing import List


class Solution:
    def twoSum(self , numbers: List[int], target: int) -> List[int]:
        # write code here
        # O(n) time, O(n) space
        visited = {} # key:val, value:[index1, index2...]
        for i in range(len(numbers)):
            if numbers[i] not in visited:
                visited[numbers[i]] = [i]
            else:
                visited[numbers[i]].append(i)
            if target - numbers[i] in visited:
                if target - numbers[i] != numbers[i]:
                    j = visited[target - numbers[i]][0]
                    if i < j:
                        return [i + 1, j + 1]
                    else:
                        return [j + 1, i + 1]
                elif target - numbers[i] == numbers[i]:
                    if len(visited[numbers[i]]) > 1:
                        return [visited[numbers[i]][0] + 1, visited[numbers[i]][1] + 1]
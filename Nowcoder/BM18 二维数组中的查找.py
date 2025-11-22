#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param target int整型
# @param array int整型二维数组
# @return bool布尔型
#
from typing import List


class Solution:
    def Find(self, target: int, array: List[List[int]]) -> bool:
        # write code here

        # edge case
        if len(array) == 0 or len(array[0]) == 0:
            return False
        if target < array[0][0] or target > array[-1][-1]:
            return False

        i = 0
        j = len(array[0]) - 1
        while i <= len(array) - 1 and j >= 0:
            if array[i][j] == target:
                return True
            elif array[i][j] > target:
                j -= 1
            elif array[i][j] < target:
                i += 1
        return False


# binary search, O(nlog(m)) for worst case
class Solution:
    def Find(self , target: int, array: List[List[int]]) -> bool:
        # write code here

        # edge case
        if len(array) == 0 or len(array[0]) == 0:
            return False
        if target < array[0][0] or target > array[-1][-1]:
            return False


        for line in array:
            if target >= line[0] and target <= line[-1]:
                left = 0
                right = len(line) - 1
                mid = 0
                while left <= right:
                    mid = (left + right) // 2
                    if target == line[mid]:
                        return True
                    elif target > line[mid]:
                        left = mid + 1
                    elif target < line[mid]:
                        right = mid - 1

        return False

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param num int整型一维数组
# @return int整型二维数组
#
from typing import List


class Solution:
    def permuteUnique(self , num: List[int]) -> List[List[int]]:
        # write code here
        result = []
        added = set()
        def help(curr, remain):
            if remain == []:
                if tuple(curr) not in added:
                    added.add(tuple(curr))
                    result.append(curr)
                return
            else:
                for i in range(len(remain)):
                    new_curr = curr[:]
                    new_curr.append(remain[i])
                    new_remain = remain[:i] + remain[i + 1:]
                    help(new_curr, new_remain)
        help([], num)
        result.sort()
        return result
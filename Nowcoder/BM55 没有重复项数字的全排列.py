#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param num int整型一维数组
# @return int整型二维数组
#
from typing import List


class Solution:
    def permute(self , num: List[int]) -> List[List[int]]:
        # write code here
        result = []
        def help(curr, remain):
            if remain == []:
                result.append(curr)
                return
            else:
                for i in range(len(remain)):
                    new_curr = curr[:]
                    new_curr.append(remain[i])
                    new_remain = remain[:i] + remain[i + 1:]
                    help(new_curr, new_remain)
        help([], num)
        return result
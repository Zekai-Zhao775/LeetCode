#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param str string字符串
# @return string字符串一维数组
#
from typing import List


class Solution:
    def Permutation(self, str: str) -> List[str]:
        # write code here
        result = []
        added = set()

        def help(curr: list, remain: list):
            if remain == []:
                temp = "".join(curr)
                if temp not in added:
                    result.append(temp)
                    added.add(temp)
                    return
            else:
                for i in range(len(remain)):
                    new_curr = curr[:]
                    new_curr.append(remain[i])
                    new_remain = remain[:i] + remain[i + 1:]
                    help(new_curr, new_remain)

        help([], list(str))
        return result
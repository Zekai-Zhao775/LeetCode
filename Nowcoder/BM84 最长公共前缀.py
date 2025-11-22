#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param strs string字符串一维数组
# @return string字符串
#
from typing import List


class Solution:
    def longestCommonPrefix(self , strs: List[str]) -> str:
        # write code here
        if len(strs) == 0:
            return ""
        prefix = strs[0]
        for s in strs:
            for i in range(min(len(prefix), len(s))):
                if prefix[i] != s[i]:
                    prefix = prefix[0:i]
                    break
            # shorten it
            prefix = prefix[0:min(len(prefix), len(s))]
        return prefix
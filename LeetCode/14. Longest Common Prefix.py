from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        i, j = 0, 0
        break_i = -1
        while i < len(strs[0]):
            j = 0
            while j < len(strs):
                if len(strs[j]) <= i or strs[j][i] != prefix[i]:
                    break_i = 1
                    break
                j += 1
            if break_i == 1:
                break
            i += 1
        return prefix[0:i]

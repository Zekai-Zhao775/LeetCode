class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # edge case
        if len(s) <= 1:
            return len(s)
        elif len(s) == 2:
            if s[0] == s[1]:
                return 1
            else:
                return 2

        substring = set()
        substring.add(s[0])
        len_max = 0
        i = 0
        j = 1
        while j < len(s):
            if s[j] not in substring:
                substring.add(s[j])
                j += 1
                len_cur = j - i
                if len_cur > len_max:
                    len_max = len_cur
            elif s[j] in substring:
                substring.remove(s[i])
                i += 1
        return len_max
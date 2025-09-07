class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        # edge case
        if len(s) > len(t) and len(s) - len(t) > 1:
            return False
        if len(t) > len(s) and len(t) - len(s) > 1:
            return False
        if s == t:
            return False
        if len(s) == 0 and len(t) == 1:
            return True
        if len(s) == 1 and len(t) == 0:
            return True

        # same len
        if len(s) == len(t):
            count_diff = 0
            for i in range(len(s)):
                if s[i] != t[i]:
                    count_diff += 1
            if count_diff > 1:
                return False

        # diff len, need add
        # first diff, add same
        if len(s) != len(t):
            if len(s) > len(t):
                s_l = s
                s_s = t
            else:
                s_l = t
                s_s = s
            count_diff = 0
            for i in range(len(s_l) - 1):
                # if i == len(s_s) - 1:
                #     if count_diff == 0:
                #         return True
                #     if count_diff > 0:
                #         return False
                if s_l[i] == s_s[i - count_diff]:
                    continue
                else:
                    count_diff += 1
                    if count_diff >= 2:
                        return False
            if count_diff == 0:
                return True
            else:
                if s_l[-1] == s_s[-1]:
                    return True
                else:
                    return False

        return True
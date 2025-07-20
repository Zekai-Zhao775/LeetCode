class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) == 1 and len(needle) == 1:
            if haystack == needle:
                return 0
            else:
                return -1

        # Brute Force O(m * n)

        # KMP O(m + n)
        # Longest Proper Prefix which is also Suffix
        # LPS
        # "sadbutsad"
        # 0,0,0,0,0,0,1,2,3
        lps = [0] * len(needle)
        len_ = 0
        i = 1
        while i < len(needle):
            if needle[i] == needle[len_]:
                len_ += 1
                lps[i] = len_
                i += 1
            else:
                if len_ == 0:
                    i += 1
                else:
                    # same logic as below
                    # image the prefix as needle here
                    len_ = lps[len_ - 1]

        print(lps)

        # matching
        i, j = 0, 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == len(needle):
                    return i - j
            else:
                if j != 0:
                    j = lps[j - 1]
                elif j == 0:
                    i += 1

        return -1
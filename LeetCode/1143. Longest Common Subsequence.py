class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dp[m][n] represents the length of longest common subsequence
        # of string text1[m:] and text[n:]
        # dp[m][n] = if text1[m]==text2[n]  + dp[m + 1][n + 1]
        # if m == len(text1) - 1, dp[m][n] = if text1[m] in text2[n:]
        # if n == len(text2) - 1, dp[m][n] = if text2[n] in text1[m:]
        # from m == len(text1) - 1 to m == 0 to give dp value so it's O[n]
        # same for n
        len_text1 = len(text1)
        len_text2 = len(text2)
        dp = [[-1 for _ in range(len_text2)] for _ in range(len_text1)]

        isInStringFlag = 0
        i = len_text1 - 1
        j = len_text2 - 1
        while j >= 0:
            if text1[i] == text2[j]:
                isInStringFlag = 1
            dp[i][j] = isInStringFlag
            j -= 1
        isInStringFlag = 0
        i = len_text1 - 1
        j = len_text2 - 1
        while i >= 0:
            if text1[i] == text2[j]:
                isInStringFlag = 1
            dp[i][j] = isInStringFlag
            i -= 1

        # print(dp)

        def dpHelp(m, n):
            if dp[m][n] != -1:
                return dp[m][n]
            elif m == len_text1 - 1 or n == len_text2 - 1:
                return dp[m][n]
            else:
                if text1[m] == text2[n]:
                    dp[m][n] = 1 + dpHelp(m + 1, n + 1)
                    return dp[m][n]
                else:
                    # if text1[m] is matched in text2[n:], then skip text1[m] will cause dp[m + 1][n] -1
                    # if text2[n] is matched in text1[m:], then skip text1[m] will cause dp[m][n + 1] -1
                    # but m and n can't be matched at the same time only if they are the same (they match with each other)
                    # so dp[m][n] =  max(dpHelp(m, n + 1), dpHelp(m + 1, n))
                    dp[m][n] = max(dpHelp(m, n + 1), dpHelp(m + 1, n))
                    return dp[m][n]

        return dpHelp(0, 0)



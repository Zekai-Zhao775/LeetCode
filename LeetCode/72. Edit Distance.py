class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len_word1 = len(word1)
        len_word2 = len(word2)

        # dp[m][n] represents minDistance of text1[m:] and text2[n:]
        # add edges to handle null string ""
        dp = [[-1 for _ in range(len_word2 + 1)] for _ in range(len_word1 + 1)]

        # give edge case value
        i, j = 0, len_word2
        while i < len_word1 + 1:
            dp[i][j] = len_word1 - i
            i += 1
        i, j = len_word1, 0
        while j < len_word2 + 1:
            dp[i][j] = len_word2 - j
            j += 1

        def minD(m, n):
            if dp[m][n] != -1:
                return dp[m][n]
            else:
                if word1[m] == word2[n]:
                    # no need to do anything
                    dp[m][n] = minD(m + 1, n + 1)
                    return dp[m][n]
                else:
                    # return min(insert, delete, replace), for each choice, use best strategy
                    # insert (insert the same as word2[n])
                    insert = 1 + minD(m, n + 1)
                    # delete
                    delete = 1 + minD(m + 1, n)
                    # replace (replace the same as word2[n])
                    replace = 1 + minD(m + 1, n + 1)
                    dp[m][n] = min(insert, delete, replace)
                    return dp[m][n]

        return minD(0, 0)
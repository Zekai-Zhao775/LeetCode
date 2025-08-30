from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # wordDict to set
        w_d = set()
        for word in wordDict:
            w_d.add(word)

        # dp[m], can s[m:] be segmented?
        dp = [None for _ in range(len(s))]

        def dp_help(m: int):
            if dp[m] != None:
                return dp[m]
            else:
                i = 1
                flag_word_find = -1
                while m + i <= len(s):
                    word = s[m:m + i]
                    if word in w_d:
                        flag_word_find = 1
                        if m + i == len(s):
                            dp[m] = True
                        dp[m] = dp[m] or dp_help(m + i)
                    i += 1
                if flag_word_find == -1:
                    dp[m] = False
                return dp[m]

        return dp_help(0)
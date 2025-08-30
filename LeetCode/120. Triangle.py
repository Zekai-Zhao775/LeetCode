from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # dp[m][n]: minimum path sum from from (m,n) in triangle to bottom
        # len(triangle) = len(bottom)
        dp = [[None for _ in range(len(triangle))] for _ in range(len(triangle))]
        for i in range(len(triangle)):
            dp[-1][i] = triangle[-1][i]

        def dp_help(m: int, n: int) -> int:
            if dp[m][n] != None:
                return dp[m][n]
            else:
                dp[m][n] = triangle[m][n] + min(dp_help(m + 1, n), dp_help(m + 1, n + 1))
                return dp[m][n]

        return dp_help(0, 0)
class Solution:
    def climbStairs(self, n: int) -> int:
        # dp[m] start from m, how many ways to top
        dp = [-1 for _ in range(n)]
        dp[-1] = 1
        def dp_help(m: int):
            if dp[m] != -1:
                return dp[m]
            elif m == n - 2:
                dp[m] = 2
                return dp[m]
            else:
                dp[m] = dp_help(m + 1) + dp_help(m + 2)
                return dp[m]
        return dp_help(0)

        return 0
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # [10, 15, 20, 30]
        # dp[0] = 10, dp[1] = 15
        # dp[2] = 20 + min(dp[0] + dp[1]) = 30
        # dp[3] = 30 + min(dp[1] + dp[2]) = 45
        n = len(cost)
        dp = [-1] * n
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i - 2], dp[i - 1])

        return min(dp[n - 1], dp[n - 2])
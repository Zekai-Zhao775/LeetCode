from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        # dp[i][0 or 1] represents start day i without stock(0) or holding stock
        # the max profit it can achieve
        dp = [[-1, -1] for _ in range(len(prices))]
        dp[-1][0] = 0
        dp[-1][1] = prices[-1]
        print(dp)
        def dpHelp(day: int, state: int) -> int:
            if dp[day][state] != -1:
                return dp[day][state]
            elif state == 0:
                dp[day][state] = max(0, dpHelp(day + 1, 0), dpHelp(day + 1, 1) - prices[day])
                return dp[day][state]
            elif state == 1:
                dp[day][state] = max(0, dpHelp(day + 1, 1), dpHelp(day + 1, 0) + prices[day])
                return dp[day][state]

        return dpHelp(0, 0)
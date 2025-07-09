from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # state 0, not holding
        # state 1, holding
        n = len(prices)
        dp = [[(-6 * 10 ** 4) for _ in range(2)] for _ in range(n)]

        def maxProfit(current_day, state):
            if dp[current_day][state] != (-6 * 10 ** 4):
                return dp[current_day][state]

            if current_day == n - 1:
                if state == 0:
                    dp[current_day][state] = 0
                else:
                    if prices[current_day] > fee:
                        dp[current_day][state] = prices[current_day] - fee
                    else:
                        dp[current_day][state] = 0
                return dp[current_day][state]

            if state == 0:
                dp[current_day][state] = max(
                    maxProfit(current_day + 1, 0),
                    maxProfit(current_day + 1, 1) - prices[current_day]
                )
            else:
                dp[current_day][state] = max(
                    maxProfit(current_day + 1, 1),
                    maxProfit(current_day + 1, 0) + prices[current_day] - fee
                )
            return dp[current_day][state]

        return maxProfit(0, 0)
from typing import List

# O(n) time, O(1) space
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 10 ** 5
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            if price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit

# dp, O(n) time, O(n) space
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         if len(prices) == 1:
#             return 0
#         dp = [-1] * len(prices)
#         dp[-1] = 0
#         # print(dp)
#         def dpHelp(i: int):
#             if i < len(prices):
#                 if dp[i] != -1:
#                     return dp[i]
#                 else:
#                     if prices[i] >= prices[i + 1]:
#                         dp[i] = max(0, prices[i + 1] - prices[i] + dpHelp(i + 1))
#                         return dp[i]
#                     else:
#                         dp[i] = max(0, prices[i + 1] - prices[i] + dpHelp(i + 1))
#                         return dp[i]
#         dpHelp(0)
#         return max(dp)
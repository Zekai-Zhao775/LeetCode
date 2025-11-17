class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # if using binary tree for searching
        # each step we either choose biggest of pick smailler
        # basically brutal
        # 2^len(coins)

        # use dp[x] to store: the min count of coins to reach amount x
        # bottom-up
        # n = len(coins)
        # m = size of amount
        # O(nm)
        dp = [0] + [float('inf')] * amount

        for coin in coins:
            for num in range(coin, amount + 1):
                dp[num] = min(dp[num], dp[num - coin] + 1)

        if dp[amount] == float('inf'):
            return -1
        else:
            return dp[amount]
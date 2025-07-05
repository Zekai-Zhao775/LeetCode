class Solution:
    def tribonacci(self, n: int) -> int:
        # Top-Down DP
        # cache = [-1] * 38
        # print(cache)
        # def cacheTribonacci(n: int) -> int:
        #     if n == 0:
        #         return 0
        #     elif n == 1:
        #         return 1
        #     elif n == 2:
        #         return 1
        #     elif cache[n] != -1:
        #         return cache[n]
        #     else:
        #         cache[n] = cacheTribonacci(n - 3) + cacheTribonacci(n - 2) + cacheTribonacci(n - 1)
        #         return cache[n]

        # return cacheTribonacci(n)

        # Bottom-Up DP
        dp = [0, 1, 1]
        for i in range(3, n + 1):
            dp.append(dp[i - 3] + dp[i - 2] + dp[i - 1])
        return dp[n]
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]

        def dfs(x, y):
            if dp[x][y] != 0:
                return dp[x][y]
            elif x == m - 1 or y == n - 1:
                dp[x][y] = 1
                return 1
            else:
                dp[x][y] = dfs(x + 1, y) + dfs(x, y + 1)
                return dp[x][y]

        return dfs(0, 0)
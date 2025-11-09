from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # each stop rob and n+2, or n+1
        dp = [-1] * len(nums)
        def dp_help(i):
            if i >= len(nums):
                return 0
            if dp[i] != -1:
                return dp[i]
            else:
                dp[i] = max(nums[i] + dp_help(i + 2), dp_help(i + 1))
                return dp[i]
        dp_help(0)

        return dp[0]

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [0] * 400
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[len(nums) - 1]
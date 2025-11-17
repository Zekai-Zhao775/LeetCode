from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # bottom-up dp
        # dp[x] store: LIS end in index x
        # O(n^2)

        dp = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
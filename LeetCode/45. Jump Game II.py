from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        # dp
        dp = [-1] * len(nums)
        dp[-1] = 0

        def dpHelp(i: int) -> int:
            if i >= len(nums) - 1:
                return 0
            if dp[i] != -1:
                return dp[i]
            else:
                j = nums[i]
                # although the case is reachable, but some num in it cant be step in
                if j == 0:
                    return 1000
                steps = []
                while j >= 1:
                    steps.append(dpHelp(i + j))
                    j -= 1
                dp[i] = min(steps) + 1
                return dp[i]

        return dpHelp(0)
# greedy, O(n) time, O(1) space
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farest = 0
        for i, num in enumerate(nums):
            if i + num >= len(nums) - 1:
                return True
            if i + num > farest:
                farest = i + num
            elif i == farest:
                return False


# dp, O(n*m)
# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         dp = [None] * len(nums)
#         if dp[-1] != 0:
#             dp[-1] = True
#         else:
#             dp[-1] = False
#         # print(dp)

#         def dpHelp(i: int) -> bool:
#             if i > len(nums) - 1:
#                 return dp[-1]
#             if dp[i] != None:
#                 return dp[i]
#             else:
#                 j = nums[i]
#                 while j >= 1:
#                     if dpHelp(i + j):
#                         dp[i] = True
#                         return dp[i]
#                     j -= 1
#                 dp[i] = False
#                 return dp[i]
#         return dpHelp(0)
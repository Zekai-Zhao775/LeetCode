from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # use prefix and suffix, O(n) time O(n) space
        # prefix (), 1, 1*2, 1*2*3, 1*2*3*4
        # suffix (), 5, 5*4, 5*4*3, 5*4*3*2
        # reverse suffix
        # suffix 5*4*3*2, 5*4*3, 5*4, 5, ()
        # prefix * suffix
        prefix = [1]
        suffix = [1]
        for i in range(len(nums) - 1):
            prefix.append(prefix[-1] * nums[i])
            suffix.append(suffix[-1] * nums[-i - 1])
        # print(prefix)
        # print(suffix)
        result = []
        for i in range(len(nums)):
            result.append(prefix[i] * suffix[-i - 1])
        return result

# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         # dp?
#         # dp(2, 3, 4), dp(1, 3, 4), dp(1, 2, 4)
#         # dp(2) dp(3, 4) dp(1) dp(3, 4) dp(1) dp(2, 4)
#         # O(n*n) time and O(n*n) space
#         dp = defaultdict()

#         def dpHelp(t: tuple) -> int:
#             if len(t) == 1:
#                 dp[t] = t[0]
#                 return t[0]
#             elif t in dp:
#                 return dp[t]
#             else:
#                 dp[t] = t[0] * dpHelp(t[1:])
#                 return dp[t]

#         result = []
#         for i in range(len(nums)):
#             result.append(dpHelp(tuple(nums[:i] + nums[i + 1:])))
#         return result


# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         product = 1
#         for num in nums:
#             product *= num
#         result = []

#         product_temp = 1
#         for i in range(len(nums)):
#             if nums[i] != 0:
#                 result.append(int(product / nums[i]))
#             else:
#                 product_temp = 1
#                 for j in range(len(nums)):
#                     if j != i:
#                         product_temp *= nums[j]
#                 result.append(int(product_temp))

#         return result
from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        len_nums = len(nums)
        i = len_nums - 1
        while i >= 2:
            # if a >= b >= c, only check b + c > a
            if nums[i - 1] + nums[i - 2] > nums[i]:
                return nums[i - 1] + nums[i - 2] + nums[i]
            i -= 1
        return 0

# Time Limit Exceeded O(n³)
# class Solution:
#     def largestPerimeter(self, nums: List[int]) -> int:
#         nums.sort()
#         len_nums = len(nums)
#         i = len_nums - 1
#         j = 0
#         k = 0

#         while i >= 2:
#             j = i - 1
#             while j >= 1:
#                 k = j - 1
#                 while k >= 0:
#                     if nums[i] + nums[j] > nums[k] and nums[i] + nums[k] > nums[j] and nums[j] + nums[k] > nums[i]:
#                         return nums[i] + nums[j] + nums[k]
#                     k -= 1
#                 j -= 1
#             i -= 1

#         return 0
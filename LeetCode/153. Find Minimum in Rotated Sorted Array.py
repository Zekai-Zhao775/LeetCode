# 8:25-8:36, 11mis
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # find first element that is smaller than previous one

        # edge case
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return min(nums)
        if nums[-1] > nums[0]:
            # no rotation or rotate len(nums) * n times
            return nums[0]

        left = 0
        mid = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            elif nums[mid] <= nums[-1]:
                right = mid - 1
            elif nums[mid] >= nums[0]:
                left = mid + 1
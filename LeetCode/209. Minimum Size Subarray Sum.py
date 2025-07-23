from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # two pointer, O(n)
        # edge case
        if len(nums) == 1:
            if nums[0] >= target:
                return 1
            else:
                return 0

        i = 0
        j = 1
        sum_subarray = nums[i] + nums[j]
        len_min = len(nums) + 1

        if nums[0] >= target or nums[1] >= target:
            return 1
        elif sum_subarray >= target:
            return 2
        elif len(nums) == 2:
            return 0

        while j < len(nums):
            if sum_subarray < target:
                j += 1
                if j == len(nums):
                    break
                sum_subarray += nums[j]
            elif sum_subarray >= target:
                len_cur = j - i + 1
                if len_cur < len_min:
                    len_min = len_cur
                sum_subarray -= nums[i]
                i += 1
        if len_min == len(nums) + 1:
            return 0
        else:
            return len_min
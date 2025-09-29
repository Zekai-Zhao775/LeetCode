from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # edge case
        if target <= nums[0]:
            return 0
        if target == nums[-1]:
            return len(nums) - 1
        if target > nums[-1]:
            return len(nums)

        left = 0
        right = len(nums) - 1
        mid = 0
        # find first num > target
        # we can check the num before to see if it's == target
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        if nums[left - 1] != target:
            return left
        else:
            return left - 1
# 8:07-8:21, 14mins
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # if we found the target then expand it like scanning, then worst case O(n)
        # instead we do two binary search
        # first search the first element that is the target
        # second search the last element that is the target

        # edge case
        if len(nums) == 0:
            return [-1, -1]
        elif len(nums) == 1:
            if nums[0] == target:
                return [0, 0]
        elif target > nums[-1] or target < nums[0]:
            return [-1, -1]
        # we can't handle taget == edge here, since it will make it O(n)

        # first search the first element that is the target
        left = 0
        mid = 0
        right = len(nums) - 1
        start = -1
        if nums[0] == target:
            start = 0
        else:
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target and nums[mid - 1] != target:
                    start = mid
                    break
                elif nums[mid] == target and nums[mid - 1] == target:
                    right = mid - 1
                elif nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
        if start == -1:
            return [-1, -1]

        # second search the last element that is the target
        left = 0
        mid = 0
        right = len(nums) - 1
        end = -1
        if nums[-1] == target:
            end = len(nums) - 1
        else:
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target and nums[mid + 1] != target:
                    end = mid
                    break
                elif nums[mid] == target and nums[mid + 1] == target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
        return [start, end]
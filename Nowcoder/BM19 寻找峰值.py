#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param nums int整型一维数组
# @return int整型
#
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # write code here
        # can't scan, then it will be O(n) not O(logn)
        # binary search, but how?
        # always looking for bigger side, cause the edge is always smaller, so bigger side guarantee a peak
        # if the left and right of a mid is bigger, pick any will work
        # also nums[i] != nums[i + 1] so peak always exsit

        # edge case
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            if nums[0] > nums[1]:
                return 0
            else:
                return 1

        left = 0
        right = len(nums) - 1
        mid = 0
        while left <= right:
            mid = (left + right) // 2
            if mid == 0:
                if nums[mid] > nums[mid + 1]:
                    return 0
                elif nums[mid] < nums[mid + 1]:
                    left = mid + 1
            elif mid == len(nums) - 1:
                if nums[mid] > nums[mid - 1]:
                    return len(nums) - 1
                elif nums[mid] < nums[mid - 1]:
                    right = mid - 1
            else:
                if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                    return mid
                elif nums[mid] < nums[mid + 1]:
                    left = mid + 1
                elif nums[mid] < nums[mid - 1]:
                    right = mid - 1


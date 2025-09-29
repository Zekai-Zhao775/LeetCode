from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # two binary search
        # first search the index
        # then convert the left, mid, right with this index included without making new nums list

        # edge case
        if len(nums) == 1:
            if target == nums[0]:
                return 0
            else:
                return -1
        elif len(nums) == 2:
            if target == nums[0]:
                return 0
            elif target == nums[1]:
                return 1
            else:
                return -1

        # search the index
        left = 0
        right = len(nums) - 1
        mid = 0
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid - 1] and mid + 1 > len(nums) - 1:
                index = mid
                break
            elif nums[mid] < nums[mid - 1] and nums[mid] < nums[mid + 1]:
                index = mid
                break
            elif nums[mid] < nums[0]:
                right = mid - 1
            elif nums[mid] > nums[-1]:
                left = mid + 1
            else:
                index = 0
                break

        # right list: nums[index:] + nums[:index]
        # search the target

        # edge case
        if target < nums[index] or target > nums[index - 1]:
            return -1
        elif target == nums[index]:
            return index
        elif target == nums[index - 1]:
            return (index - 1) % (len(nums))

        left = 0
        right = len(nums) - 1
        mid = 0
        while left <= right:
            mid = (left + right) // 2
            mid_converted = (mid + index) % (len(nums))
            if target == nums[mid_converted]:
                return mid_converted
            elif target < nums[mid_converted]:
                right = mid - 1
            elif target > nums[mid_converted]:
                left = mid + 1
        return -1
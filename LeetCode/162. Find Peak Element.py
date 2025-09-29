from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # pick a place in the middle, then the side that't bigger then this place must have one peek
        # cause nums[-1] = nums[n] = -∞
        # if both sides bigger, we always choose right side

        # edge case
        if len(nums) == 1:
            return 0

        left = 0
        right = len(nums) - 1
        mid = 0

        while left <= right:
            mid = (left + right) // 2
            if mid - 1 < 0 and nums[mid] > nums[mid + 1]:
                return mid
            elif mid + 1 > len(nums) - 1 and nums[mid] > nums[mid - 1]:
                return mid
            elif nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid + 1] > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # O(log n), so must be binary

        # nums[i] != nums[i + 1]
        # so when we pick middle,
        # if the neighbor is bigger
        # if it's monotonically increasing
        # then the peak is at the edge, we pick the right side
        # if it's not monotonically increasing, there must be peak inside it, we still peak the right side
        start = 0
        len_nums = len(nums)
        end = len_nums - 1

        if len_nums == 1:
            return 0

        while start != end:
            middle = (start + end) // 2
            if middle == 0:
                if nums[middle] > nums[middle + 1]:
                    return middle
                else:
                    start = middle + 1
            elif middle == len_nums - 1:
                if nums[middle] > nums[middle - 1]:
                    return middle
                else:
                    end = middle - 1
            elif nums[middle] > nums[middle + 1] and nums[middle] > nums[middle - 1]:
                return middle
            elif nums[middle] > nums[middle + 1] and nums[middle] < nums[middle - 1]:
                end = middle - 1
            elif nums[middle] < nums[middle + 1] and nums[middle] > nums[middle - 1]:
                start = middle + 1
            elif nums[middle] < nums[middle + 1] and nums[middle] < nums[middle - 1]:
                start = middle + 1

        return start



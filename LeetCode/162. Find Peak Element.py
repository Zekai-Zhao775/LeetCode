from typing import List


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



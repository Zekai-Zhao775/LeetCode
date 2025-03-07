from typing import List


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        result = []
        missing = []

        if nums == []:
            return [[lower, upper]]

        if nums[0] > lower:
            missing = []
            missing.append(lower)
            missing.append(nums[0] - 1)
            result.append(missing)

        i = 0
        while i < len(nums) - 1:
            if nums[i + 1] - 1 >= nums[i] + 1:
                missing = []
                missing.append(nums[i] + 1)
                missing.append(nums[i + 1] - 1)
                result.append(missing)
            i += 1

        if nums[len(nums) - 1] < upper:
            missing = []
            missing.append(nums[len(nums) - 1] + 1)
            missing.append(upper)
            result.append(missing)

        return result

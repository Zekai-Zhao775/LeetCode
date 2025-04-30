from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # sliding window O(n)
        sumMax = sum(nums[:k])
        sumTemp = sumMax
        for i in range(len(nums) - k):
            sumTemp = sumTemp - nums[i] + nums[i + k]
            if sumTemp > sumMax:
                sumMax = sumTemp
        return sumMax / k
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # can be time O(n*n)
        result = []
        nums.sort()
        # print(nums)

        # -> num[i] + num[j] = -num[k]
        k = 0
        while k < len(nums) - 1:
            if k > 0 and nums[k] == nums[k - 1]:
                k += 1
                continue
            i = k + 1
            j = len(nums) - 1
            while i < j:
                s = nums[i] + nums[j] + nums[k]
                if s == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
                elif s > 0:
                    j -= 1
                elif s < 0:
                    i += 1
            k += 1

        return result
from typing import List


class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        # sliding window
        # O(n*m)
        i = 0
        n = len(nums)
        m = len(pattern)
        size = m + 1
        count = 0
        while i + size - 1 < n:
            flag = 1
            j = 0
            while j < m:
                if pattern[j] == 1:
                    if nums[i + j + 1] <= nums[i + j]:
                        flag = -1
                        break
                elif pattern[j] == 0:
                    if nums[i + j + 1] != nums[i + j]:
                        flag = -1
                        break
                elif pattern[j] == -1:
                    if nums[i + j + 1] >= nums[i + j]:
                        flag = -1
                        break
                j += 1
            if flag == 1:
                count += 1
            i += 1
        return count
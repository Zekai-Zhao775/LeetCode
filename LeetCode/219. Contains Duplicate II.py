from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums_dict = {}
        for i in range(len(nums)):
            if nums[i] not in nums_dict:
                nums_dict[nums[i]] = i
            else:
                if i - nums_dict[nums[i]] <= k:
                    return True
                nums_dict[nums[i]] = i
        return False
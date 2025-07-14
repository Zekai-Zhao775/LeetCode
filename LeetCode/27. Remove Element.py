from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count_move = 0
        for i in range(len(nums)):
            if nums[i] == val:
                count_move += 1
            else:
                nums[i - count_move] = nums[i]
            i += 1
        return len(nums) - count_move
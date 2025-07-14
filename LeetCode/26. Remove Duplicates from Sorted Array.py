from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last_num = -101
        count_move = 0
        for i in range(len(nums)):
            if nums[i] == last_num:
                count_move += 1
            else:
                nums[i - count_move] = nums[i]
                last_num = nums[i]
            i += 1
        return len(nums) - count_move
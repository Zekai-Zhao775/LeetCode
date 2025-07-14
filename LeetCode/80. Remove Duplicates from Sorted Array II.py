from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last_num = - 10 ** 4 - 1
        count_last_num = 0
        count_remove = 0
        for i in range(len(nums)):
            if nums[i] == last_num and count_last_num < 2:
                nums[i - count_remove] = nums[i]
                count_last_num += 1
            elif nums[i] == last_num and count_last_num == 2:
                count_remove += 1
            else:
                count_last_num = 1
                last_num = nums[i]
                nums[i - count_remove] = nums[i]
            i += 1
        print(nums)
        return len(nums) - count_remove
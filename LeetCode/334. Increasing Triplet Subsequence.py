from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # O(n^3)
        # i = 0
        # j = 0
        # k = 0
        # while i < len(nums):
        #     j = i + 1
        #     while j < len(nums):
        #         if nums[i] < nums[j]:
        #             k = j + 1
        #             while k < len(nums):
        #                 if nums[j] < nums[k]:
        #                     return True
        #                 k += 1
        #         j += 1
        #     i += 1

        # return False

        # O(n)
        num_min = 2 ** 31 - 1
        num_min_second = 2 ** 31 - 1

        for num in nums:
            if num <= num_min:
                num_min = num
            elif num < num_min_second:
                num_min_second = num  # update doesn't effect the fact there was a increasing pair
            elif num > num_min_second:
                return True
        return False

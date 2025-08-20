from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # sort, nlogn

        nums_set = set()
        checked_set = set()
        len_max = 0

        for num in nums:
            if num not in nums_set:
                nums_set.add(num)

        for num in nums_set:
            if num in checked_set:
                continue
            elif num - 1 in nums_set:
                checked_set.add(num)
            else:
                len_current = 0
                while num in nums_set:
                    checked_set.add(num)
                    len_current += 1
                    num += 1
                if len_current > len_max:
                    len_max = len_current
        return len_max
from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # O(nlog(n)) two pointer, but with sort
        # nums.sort()
        # index = len(nums) - 1
        # for i in range(len(nums)):
        #     if nums[i] >= k:
        #         index = i - 1
        #         break
        # print(index)
        # i = 0
        # j = index
        # count = 0
        # while i < j:
        #     if nums[i] + nums[j] > k:
        #         j -= 1
        #     elif nums[i] + nums[j] < k:
        #         i += 1
        #     else:
        #         count += 1
        #         j -= 1
        #         i += 1
        # return count

        #O(n) hashmap using dict, but O(n) extra space
        freq = {}
        count = 0
        for num in nums:
            pair = k - num
            if freq.get(pair, 0) != 0:
                count += 1
                freq[pair] -= 1
            elif freq.get(num, 0) != 0:
                freq[num] += 1
            else:
                freq[num] = 1
        return count
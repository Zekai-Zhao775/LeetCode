from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # need O(n) time O(1) space solution

        # sort and pick middle, O(nlogn) time O(1) space
        # nums.sort()
        # return nums[len(nums) // 2]

        # make dict, O(n) time and O(n) space
        # nums_dict = defaultdict(int)
        # for num in nums:
        #     nums_dict[num] += 1
        # for key in nums_dict:
        #     if nums_dict[key] >= len(nums) // 2 + 1:
        #         return key

        # Boyer–Moore majority vote algorithm
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
                count += 1
            elif num == candidate:
                count += 1
            else:
                count -= 1
        return candidate
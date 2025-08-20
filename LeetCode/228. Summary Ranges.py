from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        temp = []
        i = 0
        while i < len(nums):
            if len(temp) == 0 or temp[-1] == nums[i] - 1 or temp[-1] == nums[i]:
                temp.append(nums[i])
            elif temp[-1] < nums[i] - 1:
                if len(temp) == 1:
                    result.append(str(temp[0]))
                else:
                    result.append(str(temp[0]) + "->" + str(temp[-1]))
                temp = [nums[i]]
            i += 1

        if len(temp) != 0:
            if len(temp) == 1:
                result.append(str(temp[0]))
            else:
                result.append(str(temp[0]) + "->" + str(temp[-1]))

        return result
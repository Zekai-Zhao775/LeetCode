#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param nums int整型一维数组
# @return int整型
#
from typing import List


class Solution:
    def minNumberDisappeared(self , nums: List[int]) -> int:
        # write code here

        # can't sort
        # O(1), so in place modify
        # O(n) time, iterate once or iterate every element one time
        # len(nums) = n, answer is between [1, n + 1]
        # if 1 in it, we put it in nums[1 - 1]
        # if n in it, we put it in nums[n - 1]
        # iterate
        # if nums[i] != i, that's the answer
        n = len(nums)
        for i in range(len(nums)):
            val = nums[i]
            while val >= 1 and val <= n and nums[val - 1] != val:
                temp = nums[val - 1]
                nums[val - 1] = val
                val = temp
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return n + 1

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param nums int整型一维数组
# @return int整型一维数组
#
from typing import List


class Solution:
    def FindNumsAppearOnce(self, nums: List[int]) -> List[int]:
        # write code here
        # use xor, can find the number that one number shows one time, not really for this question?
        # use a dict, then there will be O(n) space, worst case it will be O(1/n) even we del it dynamitly
        # we use apply xor to each number at each position, but then time will be O(n^2)

        # still need use xor
        # old way we only have A^B after
        # we get lowest 1 from it, use this low_bit to seperate the group into two parts
        # do the same thing to two parts we get A and B

        a_xor_b = 0
        # O(n)
        for num in nums:
            a_xor_b ^= num

        low_bit = 0b1
        while a_xor_b & low_bit == 0:
            low_bit <<= 1

        a = 0
        b = 0
        for num in nums:
            if num & low_bit == 0:
                a ^= num
            else:
                b ^= num

        if a <= b:
            return [a, b]
        else:
            return [b, a]
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # need O(n) time and O(1) space
        # dictionary O(n) time O(n) space, skip

        # use list itself to tract single
        # pop it when see it again, nums[i] in nums[:i]?
        # O(n*n) time, O(1)

        # sort it first then scan, O(logn) time and O(1) space

        # use xor
        # xor ^ satisfies both the commutative and associative laws
        # commutative law 交换律
        # associative laws 结合律
        # a xor a = 0, a ^ a = 0
        # a xor 0 = a, a ^ 0 = a
        # 0 xor 0 = 0, 0 ^ 0 = 0
        result = 0
        for num in nums:
            result ^= num
        return result
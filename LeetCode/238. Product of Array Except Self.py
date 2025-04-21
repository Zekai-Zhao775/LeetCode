from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        for num in nums:
            product *= num
        result = []

        product_temp = 1
        for i in range(len(nums)):
            if nums[i] != 0:
                result.append(int(product / nums[i]))
            else:
                product_temp = 1
                for j in range(len(nums)):
                    if j != i:
                        product_temp *= nums[j]
                result.append(int(product_temp))

        return result
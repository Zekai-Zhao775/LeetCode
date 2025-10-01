from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # xor won't work here
        # count 1 in each position of binary form of each num
        # can't divided by 3 then it's the 1 in the num that appears only once

        store = [0 for i in range(32)]

        def count_one(num, store):
            # -231 <= nums[i] <= 231 - 1
            # use 32 bits
            if num >= 0:
                num_b = bin(num)[2:].zfill(32)  # 0bxxxx
            else:
                num_b = bin(num)[3:].zfill(
                    32)  # -0bxxxx, we convert to unsigned here, and later scan to find positive or negitive

            for i in range(len(num_b)):
                if num_b[i] == "1":
                    store[i] += 1
            return

        for num in nums:
            count_one(num, store)

        for i in range(len(store)):
            store[i] = str(store[i] % 3)

        result = int("".join(store), 2)
        if nums.count(result) == 1:
            return result
        else:
            return result * -1
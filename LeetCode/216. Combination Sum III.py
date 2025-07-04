from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # edge
        if sum(nums) < n:
            return []
        if n < (1 + k) * k / 2:
            return []

        path = []
        result = []

        def possibleCombinations(left_k: int, nums: List[int]):
            if left_k == 1:
                for num in nums:
                    path.append(num)
                    sum_path = sum(path)
                    if sum_path == n:
                        result.append(path[:])
                        path.pop()
                        return
                    elif sum_path > n:
                        path.pop()
                        return
                    else:
                        path.pop()
            else:
                i = 0
                while i < len(nums):
                    path.append(nums[i])
                    new_nums = nums[i + 1:]
                    possibleCombinations(left_k - 1, new_nums)
                    path.pop()
                    i += 1

        possibleCombinations(k, nums)

        return result
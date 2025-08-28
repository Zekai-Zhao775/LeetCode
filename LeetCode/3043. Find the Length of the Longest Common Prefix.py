from typing import List


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        set_1 = set()
        set_2 = set()
        for i in range(len(arr1)):
            arr1[i] = str(arr1[i])
            for j in range(len(arr1[i])):
                set_1.add(arr1[i][:j + 1])
        for i in range(len(arr2)):
            arr2[i] = str(arr2[i])
            for j in range(len(arr2[i])):
                set_2.add(arr2[i][:j + 1])
        prefix_max = 0
        for prefix in set_2:
            if prefix in set_1 and len(prefix) > prefix_max:
                prefix_max = len(prefix)
        return prefix_max

# class Solution:
#     def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
#         # can't be O(n^2)
#         for i in range(len(arr1)):
#             arr1[i] = str(arr1[i])
#         for i in range(len(arr2)):
#             arr2[i] = str(arr2[i])

#         prefix_max = 0
#         prefix = 0
#         for i in range(len(arr1)):
#             for j in range(len(arr2)):
#                 if prefix_max > len(arr1[i]) or prefix_max > len(arr2[j]):
#                     continue
#                 prefix = self.prefix(arr1[i], arr2[j])
#                 if prefix > prefix_max:
#                     prefix_max = prefix
#         return prefix_max

#     def prefix(self, num1: str, num2: str) -> int:
#         count = 0
#         for i in range(min(len(num1), len(num2))):
#             if num1[i] != num2[i]:
#                 break
#             else:
#                 count += 1
#         return count
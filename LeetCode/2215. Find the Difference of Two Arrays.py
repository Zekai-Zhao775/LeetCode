from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer0 = set()
        answer1 = set()
        for num in nums1:
            if num not in nums2:
                answer0.add(num)
        for num in nums2:
            if num not in nums1:
                answer1.add(num)
        return [list(answer0), list(answer1)]

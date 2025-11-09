import heapq
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # since n is 10^5, can't be O(n^2)
        # how to solve in O(log(n))?
        # or how to select best path to stop at k?
        # also how to use heap?
        # 00 01 02 03
        # 10 11 12 13
        # 20 21 22 23
        # 30 31 32 33
        # left up is always bigger than it's down or right neighbor
        # use a queue?
        # use a heapq, need to pop smallest first
        # when pushing, check visited first(set)
        # early stop at k
        # pop top(smallest), append it to result
        result = []
        visited = set()
        heap = [(nums1[0] + nums2[0], 0, 0)] # (sum, i, j)
        visited.add((0, 0))
        count = 0
        while heap and count < k:
            s, i, j = heapq.heappop(heap)
            result.append([nums1[i], nums2[j]])
            count += 1
            if i + 1 < len(nums1) and (i + 1, j) not in visited:
                heapq.heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
                visited.add((i + 1, j))
            if j + 1 < len(nums2) and (i, j + 1) not in visited:
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
                visited.add((i, j + 1))
        return result

import heapq
from typing import List


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # k = 1, O(n)
        if k == 1:
            i = 0
            max_score = 0
            temp_score = 0
            for i in range(len(nums1)):
                temp_score = nums1[i] * nums2[i]
                if temp_score > max_score:
                    max_score = temp_score
            return max_score

        # Otherwise, O(nlogn)
        # sort nums2, at the same time reorder nums1 using nums2 order O(nlogn)
        # also build nums3 with sorted nums1 O(n)
        sorted_nums2 = []
        reordered_num1 = []
        combined = []

        for i in range(len(nums1)):
            combined.append((nums2[i], nums1[i]))

        # sort in descending order
        combined.sort(reverse=True)
        for t in combined:
            sorted_nums2.append(t[0])
            reordered_num1.append(t[1])
        print(reordered_num1)
        print(sorted_nums2)

        # keep track (k-1)th biggest using heap
        # from left to right, if reordered_num1[i] > heap[0], pop heap[0], push reordered_num1[i]

        max_score = 0
        temp_score = 0
        i = k - 1
        heap = reordered_num1[:k - 1]
        heapq.heapify(heap)  # O(n)
        heap_sum = sum(heap)

        while i < len(sorted_nums2):
            temp_score = sorted_nums2[i] * (heap_sum + reordered_num1[i])
            if temp_score > max_score:
                max_score = temp_score
            if reordered_num1[i] > heap[0]:
                heap_sum = heap_sum - heap[0] + reordered_num1[i]
                # O(logn)
                heapq.heappop(heap)
                heapq.heappush(heap, reordered_num1[i])
            i += 1

        return max_score
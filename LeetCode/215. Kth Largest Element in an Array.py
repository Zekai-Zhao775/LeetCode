import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # use heap to store
        # use -1 to turn min heap into max heap
        # heapify O(n), pop k largest O(klog(n))
        for i in range(len(nums)):
            nums[i] = -nums[i]
        heapq.heapify(nums)
        for i in range(k):
            num = -heapq.heappop(nums)
        return num

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        # min heap to store kth
        # heap top is kth largest
        for i in range(k):
            heapq.heappush(heap, nums[i])

        for num in nums[k:]:
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)

        return heap[0]
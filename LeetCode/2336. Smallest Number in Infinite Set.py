import heapq


class SmallestInfiniteSet:

    def __init__(self):
        # only track add back
        self.pop_flag = 1
        self.add_back = []

    def popSmallest(self) -> int:
        if len(self.add_back) == 0:
            self.pop_flag += 1
            return self.pop_flag - 1
        else:
            return heapq.heappop(self.add_back)

    def addBack(self, num: int) -> None:
        if num not in self.add_back and num < self.pop_flag:
            heapq.heappush(self.add_back, num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
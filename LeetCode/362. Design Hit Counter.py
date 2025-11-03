from collections import deque


class HitCounter:

    def __init__(self):
        # use a deque to store all hits
        self.hits = deque()

    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        # lazy remove
        if len(self.hits) == 0:
            return 0
        else:
            while len(self.hits) > 0 and timestamp - self.hits[0] >= 300:
                self.hits.popleft()
            return len(self.hits)

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
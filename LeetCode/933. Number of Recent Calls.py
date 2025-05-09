class RecentCounter:

    def __init__(self):
        self.pingTime = [] # store each ping time


    def ping(self, t: int) -> int:
        self.pingTime.append(t)
        while self.pingTime[0] < t - 3000:
            self.pingTime.pop(0)
        return len(self.pingTime)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
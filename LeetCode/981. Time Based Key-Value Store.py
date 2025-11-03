from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.store = defaultdict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
            self.store[key].append((timestamp, value))
        else:
            self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key in self.store and self.store[key][0][0] <= timestamp:
            for i in range(len(self.store[key])):
                if self.store[key][len(self.store[key]) - 1 - i][0] <= timestamp:
                    return self.store[key][len(self.store[key]) - 1 - i][1]
        else:
            return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
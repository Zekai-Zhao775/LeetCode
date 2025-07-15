from collections import defaultdict
from random import random


class RandomizedSet:

    def __init__(self):
        self.store = defaultdict(int)
        self.store_list = []

    def insert(self, val: int) -> bool:
        if val in self.store:
            return False
        else:
            self.store_list.append(val)
            self.store[val] = len(self.store_list) - 1
            return True

    def remove(self, val: int) -> bool:
        if val not in self.store:
            return False
        else:
            # val is at the end of store_list
            if self.store[val] == len(self.store_list) - 1:
                self.store_list.pop()
                del self.store[val]
            else:
                last_val = self.store_list.pop()
                self.store[last_val] = self.store[val]
                self.store_list[self.store[last_val]] = last_val
                del self.store[val]
            return True

    def getRandom(self) -> int:
        return self.store_list[random.randint(0, len(self.store_list) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
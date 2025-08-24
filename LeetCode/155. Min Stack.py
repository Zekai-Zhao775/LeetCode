class MinStack:

    def __init__(self):
        self.store = []
        self.min = None

    def push(self, val: int) -> None:
        if self.min == None:
            self.store.append((val, val))
            self.min = val
        elif self.min <= val:
            self.store.append((val, self.min))
        elif self.min > val:
            self.store.append((val, val))
            self.min = val

    def pop(self) -> None:
        self.store.pop()
        if len(self.store) == 0:
            self.min = None
        else:
            self.min = self.store[-1][1]

    def top(self) -> int:
        return self.store[-1][0]

    def getMin(self) -> int:
        return self.store[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
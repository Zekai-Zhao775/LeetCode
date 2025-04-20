class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = []
        self.rear = -1
        self.size = k

    def enQueue(self, value: int) -> bool:
        if self.rear == self.size - 1:
            return False
        else:
            self.queue.append(value)
            self.rear += 1
            return True

    def deQueue(self) -> bool:
        if self.rear == -1:
            return False
        else:
            del self.queue[0]
            self.rear -= 1
            return True

    def Front(self) -> int:
        if self.rear == -1:
            return -1
        else:
            return self.queue[0]

    def Rear(self) -> int:
        if self.rear == -1:
            return -1
        else:
            return self.queue[self.rear]

    def isEmpty(self) -> bool:
        if self.rear == -1:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.rear == self.size - 1:
            return True
        else:
            return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
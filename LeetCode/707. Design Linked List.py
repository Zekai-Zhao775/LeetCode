from typing import List


class MyLinkedList:
    class Node:
        def __init__(self, val):
            self.val = val
            self.next = None

    def __init__(self):
        self.head = self.Node(-1)
        self.tail = self.Node(-1)
        self.head.next = self.tail
        self.length = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1
        i = 0
        node = self.head
        while i <= index:
            node = node.next
            i += 1
        return node.val

    def getAll(self) -> List[int]:
        result = []
        i = 0
        node = self.head
        while i < self.length:
            node = node.next
            result.append(node.val)
            i += 1
        return result

    def addAtHead(self, val: int) -> None:
        newNode = self.Node(val)
        newNode.next = self.head.next
        self.head.next = newNode
        self.length += 1

    def addAtTail(self, val: int) -> None:
        newNode = self.Node(-1)
        self.tail.val = val
        self.tail.next = newNode
        self.tail = self.tail.next
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index == self.length:
            self.addAtTail(val)
        elif index >= 0 and index < self.length:
            i = 0
            node = self.head
            while i < index:
                node = node.next
                i += 1
            newNode = self.Node(val)
            newNode.next = node.next
            node.next = newNode
            self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < self.length:
            i = 0
            node = self.head
            while i < index:
                node = node.next
                i += 1
            node.next = node.next.next
            self.length -= 1

obj = MyLinkedList()
print(obj.getAll())
obj.addAtHead(1)
print(obj.getAll())
obj.addAtTail(2)
print(obj.getAll())
obj.addAtTail(3)
print(obj.getAll())
obj.addAtIndex(3, 10)
print(obj.getAll())
print(obj.get(0))
print(obj.get(1))
print(obj.get(2))
print(obj.get(3))
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
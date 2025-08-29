class Node:
    def __init__(self, k=0, v=0):
        self.k = k
        self.v = v
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        # dict + doubly linked list
        # dict use key to store the node
        # value store in node
        self.dict = {}
        self.head = Node()
        self.tail = Node()
        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None
        self.capacity = capacity

    # helper function
    def _add_front(self, node: Node):
        node.prev = self.head
        node.next = self.head.next
        node.next.prev = node
        node.prev.next = node

    def _remove(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _move_to_front(self, node: Node):
        self._remove(node)
        self._add_front(node)

    def _evict_lru(self):
        node = self.tail.prev
        self._remove(node)
        del self.dict[node.k]

    def get(self, key: int) -> int:
        if key in self.dict:
            self._move_to_front(self.dict[key])
            return self.dict[key].v
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            node = self.dict[key]
            node.v = value
            self._move_to_front(node)
        else:
            if len(self.dict) < self.capacity:
                node = Node(key, value)
                self._add_front(node)
                self.dict[key] = node
            else:
                self._evict_lru()
                node = Node(key, value)
                self._add_front(node)
                self.dict[key] = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
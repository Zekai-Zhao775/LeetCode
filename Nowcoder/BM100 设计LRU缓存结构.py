class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class Solution:
    # hash map, store key:key, val:Node
    # with double linked list

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.current_size = 0
        self.list_head = Node(-1, -1)
        self.list_tail = Node(-2, -1)
        self.list_head.next = self.list_tail
        self.list_tail.prev = self.list_head
        self.map = {}

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            self.pop_from_list(node)
            self.put_head(node)
            return node.val
        else:
            return -1

    def set(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.val = value
            self.pop_from_list(node)
            self.put_head(node)
            return
        else:
            if self.current_size < self.capacity:
                node = Node(key, value)
                self.map[key] = node
                self.put_head(node)
                self.current_size += 1
                return
            else:
                self.delete_tail()
                node = Node(key, value)
                self.map[key] = node
                self.put_head(node)

    def put_head(self, node:Node):
        node.prev = self.list_head
        node.next = self.list_head.next
        self.list_head.next.prev = node
        self.list_head.next = node

    def delete_tail(self):
        prev_node = self.list_tail.prev
        prev_node.prev.next = self.list_tail
        self.list_tail.prev = prev_node.prev
        del self.map[prev_node.key]
        # help GC
        prev_node.prev = None
        prev_node.next = None

    def pop_from_list(self, node:Node):
        node.prev.next = node.next
        node.next.prev = node.prev

# Your Solution object will be instantiated and called as such:
# solution = Solution(capacity)
# output = solution.get(key)
# solution.set(key,value)
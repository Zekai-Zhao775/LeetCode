class MyHashMap:

    def __init__(self):
        n = 10 ** 6 + 1
        self.hashTable = [[-1, -1] for i in range(n)]

    def put(self, key: int, value: int) -> None:
        if self.hashTable[key][0] == -1:
            self.hashTable[key][0] = key
            self.hashTable[key][1] = value
        elif self.hashTable[key][0] == key:
            self.hashTable[key][1] = value
        # collision

    def get(self, key: int) -> int:
        if self.hashTable[key][0] == key:
            return self.hashTable[key][1]
        # collision
        else:
            return self.hashTable[key][1]

    def remove(self, key: int) -> None:
        if self.hashTable[key][0] == key:
            self.hashTable[key][0] = -1
            self.hashTable[key][1] = -1
        # collision

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
from collections import deque

class LRUCache:

    def __init__(self, capacity: int):
        self.D = deque(maxlen = capacity)
        self.V = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.V:
            idx = self.D.index(key)
            del self.D[idx]
            self.D.append(key)
            return self.V[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.V:
            idx = self.D.index(key)
            del self.D[idx]
        elif len(self.D) == self.capacity:
            del self.V[self.D.popleft()]
        self.D.append(key)
        self.V[key] = value



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

cache = LRUCache(capacity=2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))       # 返回  1
cache.put(3, 3)    # 该操作会使得密钥 2 作废
print(cache.get(2))       # 返回 -1 (未找到)
cache.put(4, 4)    # 该操作会使得密钥 1 作废
print(cache.get(1))       # 返回 -1 (未找到)
print(cache.get(3))       # 返回  3
print(cache.get(4))       # 返回  4
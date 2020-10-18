from collections import deque


class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.dic = {}
        self.q = deque()

    # @return an integer
    def get(self, key):
        if key in self.dic:
            self.q.remove(key)
            self.q.appendleft(key)
            return self.dic[key]
        return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.dic:
            self.q.remove(key)
        elif self.capacity == len(self.dic):
            keyToRemove = self.q.pop()
            del self.dic[keyToRemove]
        self.q.appendleft(key)
        self.dic[key] = value


if __name__ == '__main__':

    l = LRUCache(2)
    l.set(1, 10)
    l.set(5, 12)
    print(l.get(5))
    l.get(5)
    l.get(1)

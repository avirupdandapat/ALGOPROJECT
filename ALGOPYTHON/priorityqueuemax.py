class PQMax:
    def __init__(self, capacity):
        self.pq = [None] * (capacity + 1)
        self.N = 0

    def isEmpty(self):
        return self.N == 0

    def less(self, v, w):
        if self.pq[v] is None or self.pq[w] is None: return False
        return self.pq[v] < self.pq[w]

    def exch(self, i, j):
        swap = self.pq[i]
        self.pq[i] = self.pq[j]
        self.pq[j] = swap

    def swim(self, k):
        while k > 1 and self.less(int(k / 2), k):
            self.exch(k, int(k / 2))
            k = int(k / 2)

    def insert(self, x):
        self.N += 1
        self.pq[self.N] = x
        if self.N >= 2:
            self.swim(self.N)

    def sink(self, k):
        while 2 * k <= self.N:
            j = 2 * k
            # Check if we are going off the end of the heap and which child is larger
            if j < self.N and self.less(j, j + 1):
                j += 1
            # If k is not less than either child, then we are done
            if not self.less(k, j):
                break
            # If k is larger than a child, exchange
            self.exch(k, j)
            k = j

    def delMax(self):  # 10:03
        """Return and remove the largest key."""
        maxKey = self.pq[1]
        # Exchange root(maxKey) with node at end,
        self.exch(1, self.N)
        self.N -= 1
        # then sink new root down to where it belongs.
        self.sink(1)
        # Prevent loitering by nulling out maxKey position
        self.pq[self.N + 1] = None
        return maxKey

    def dataprint(self):
        for i in range(1, self.N + 1):
            print(self.pq[i])


if __name__ == "__main__":
    pq = PQMax(10)
    pq.insert(1)
    pq.insert(2)
    pq.insert(3)
    pq.insert(4)
    pq.insert(5)
    pq.insert(6)
    print(pq.dataprint())
    pq.delMax()
    (pq.dataprint())
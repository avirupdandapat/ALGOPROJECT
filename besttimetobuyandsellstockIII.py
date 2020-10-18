class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, a):
        m = 0
        f = [0] * len(a)
        l = float('inf')

        # Forward phase
        for i in range(len(a)):
            l = min(l, a[i])
            p = a[i] - l
            m = max(m, p)
            f[i] = m

        h = float('-inf')

        # Backward phase
        for j in range(len(a) - 1, 0, -1):
            h = max(h, a[j])
            p = h - a[j]
            m = max(m, f[j - 1] + p)

        return m

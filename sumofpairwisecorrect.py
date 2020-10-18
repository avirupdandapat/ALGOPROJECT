class Solution:
    # @param A : tuple of integers
    # @return an integer
    def hammingDistance(self, A):
        n = len(A)
        c = 0
        for i in range(32):
            mask = 1 << i
            t = 0
            for a in A:
                if mask & a:
                    print(mask, a)
                    t += 1
            c += (t * (n - t))
        return (2 * c) % 1000000007


if __name__ == "__main__":
    c = [2, 4, 6]
    print(Solution().hammingDistance(c))
    print(10 & 110)

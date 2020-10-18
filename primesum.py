class Solution:
    # @param A : integer
    # @return a list of integers
    def primesum(self, A):
        def prime(x):
            d = 2
            while d * d <= x:
                if not x % d: return False
                d += 1
            return True

        for i in range(2, A // 2 + 1):
            if prime(i) and prime(A - i): return [i, A - i]


if __name__ == "__main__":
    print(Solution().primesum(36))

class Solution:
    # @param A : integer
    # @return an integer
    def isPrime(self, A):
        if A <= 1:
            return 0
        if A == 2:
            return 1

        for i in range(2, int(A ** 0.5) + 1):
            if A % i == 0:
                return 0

        return 1


if __name__ == "__main__":
    print(Solution().isPrime(9))

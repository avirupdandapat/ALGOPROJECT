class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        res = set(A)
        for i in range(len(A)):
            s = A[i] - B
            if s in res:
                return 1
        return 0


if __name__ == '__main__':
    A = [1, 5, 3]
    print(Solution().diffPossible(A, 2))

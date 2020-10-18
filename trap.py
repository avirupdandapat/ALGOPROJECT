class Solution:
    # @param A : tuple of integers
    # @return an integer
    def trap(self, A):
        n = len(A)
        left = [0] * n
        rite = [0] * n

        left[0] = A[0]
        for i in range(1, n):
            left[i] = max(left[i - 1], A[i])

        rite[-1] = A[-1]
        for i in range(n - 2, -1, -1):
            rite[i] = max(rite[i + 1], A[i])

        ans = 0
        print(left)
        print(rite)
        for i in range(n):
            ans += min(left[i], rite[i]) - A[i]

        return ans


if __name__ == '__main__':
    A = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(Solution().trap(A))

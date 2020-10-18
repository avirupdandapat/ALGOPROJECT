class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minPathSum(self, A):
        if len(A) == 0:
            return 0
        r = len(A)
        c = len(A[0])
        dp = [[0 for p in range(len(A))] for p in range(c)]
        for i in range(r):
            for j in range(c):
                dp[i][j] += A[i][j]
                if i > 0 and j > 0:
                    dp[i][j] += min(dp[i-1][j], dp[i][j-1])
                elif i > 0:
                    dp[i][j] += dp[i - 1][j]
                elif j > 0:
                    dp[i][j] += dp[i][j-1]

        return dp[r-1][c-1]


if __name__ == '__main__':
    A = [[1, 3, 2],
         [4, 3, 1],
         [5, 6, 1]
         ]
    print(Solution().minPathSum(A))

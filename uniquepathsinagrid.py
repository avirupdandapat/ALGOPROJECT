class Solution:
    # @param A : list of list of integers
    # @return an integer
    def uniquePathsWithObstacles(self, A):
        dp = [[0 for p in range(len(A))] for p in range(len(A[0]))]
        for i in range(len(dp)):
            if A[i][0] != 1:
                dp[i][0] = 1
        for i in range(len(dp[0])):
            if A[0][i] != 1:
                dp[0][i] = 1
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if A[i][j] != 1:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[len(A) - 1][len(A[0]) - 1]


if __name__ == '__main__':
    A = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    print(Solution().uniquePathsWithObstacles(A))

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minPathSum(self, A, B):
        dp = [[0 for p in range(A)] for p in range(B)]
        for i in range(len(dp)):
            dp[i][0] = 1
        for i in range(len(dp[0])):
            dp[0][i] = 1
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[B-1][A-1]


if __name__ == '__main__':
    print(Solution().minPathSum(3, 3))
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        dp = [[0 for _ in range(len(A))] for _ in range(len(A))]

        i = 0
        for k in range(len(A)):
            for j in range(k, len(A)):
                if i == j:
                    dp[i][j] = 1
                elif A[i] == A[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
                i += 1
            i = 0
        print(dp)
        return dp[0][-1]


if __name__ == '__main__':
    A = "bebeeed"
    print(Solution().solve(A))

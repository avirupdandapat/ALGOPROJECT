class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        dp = [[0 for _ in range(len(B) + 1)] for __ in range(len(A) + 1)]
        print(dp)

        for i in range(1, len(A) + 1):
            for j in range(1, len(B) + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1

                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        print(dp)
        return dp[len(A)][len(B)]


if __name__ == '__main__':
    A = "abbcdgf"
    B = "bbadcgf"
    print(Solution().solve(A, B))

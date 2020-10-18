class Solution:
    # @param A : tuple of integers
    # @return an integer
    def solve(self, A):
        # Base case
        if len(A) < 2:
            return len(A)

        from collections import defaultdict

        dp = [defaultdict(int) for i in range(len(A))]
        max_len = 0
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                diff = A[i] - A[j]
                dp[j][diff] = max(dp[i][diff] + 1, dp[j][diff])
                print(dp)
                max_len = max(max_len, dp[j][diff])
        return max_len + 1


if __name__ == '__main__':
    A = [9, 4, 7, 2, 10]
    print(Solution().solve(A))
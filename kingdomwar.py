class Solution:
    # @param A : list of list of integers
    # @return an integer
    dp = []

    def solve(self, A):
        for r in range(len(A)):
            self.dp.append([])
            for c in range(len(A[0])):
                self.dp[r].append(A[r][c])

        maximum = -float("inf")
        R = len(A) - 1
        C = len(A[0]) - 1
        for r in range(R, -1, -1):
            for c in range(C, -1, -1):
                if r == R and c == C:
                    self.dp[r][c] = A[r][c]
                elif c < C and r < R:
                    self.dp[r][c] = self.dp[r + 1][c] + self.dp[r][c + 1] - self.dp[r + 1][c + 1] + A[r][c]
                elif c == C:
                    self.dp[r][c] = self.dp[r + 1][c] + A[r][c]
                elif r == R:
                    self.dp[r][c] = self.dp[r][c + 1] + A[r][c]
                maximum = max(maximum, self.dp[r][c])
        return maximum


if __name__ == '__main__':
    A = [[-5, -4, -1], [-3, 2, 4], [2, 5, 8]]
    print(Solution().solve(A))

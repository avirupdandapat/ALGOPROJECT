class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, N, S):
        arr = [[0 for j in range(S + 1)] for i in range(N + 1)]
        arr[0][0] = 1
        for n in range(N):
            for s in range(S):
                for digit in range(10):
                    if s + digit <= S:
                        arr[n + 1][s + digit] += arr[n][s]
                    else:
                        break
        return arr[N][S] % 1000000007

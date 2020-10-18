class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        if A == 0:
            return B

        n = len(B)
        if n == 0:
            return
        m = len(B[0])
        if m == 0:
            return
        DP = [[[0 for r in range(m)] for col in range(n)] for row in range(A+1)]
        print(DP)
        for k in range(A+1):
            for i in range(n):
                for j in range(m):
                    if k == 0:
                        DP[k][i][j] = B[i][j]
                    else:
                        cur = -9999
                        if i > 0:
                            cur = max(cur, int(DP[k - 1][i - 1][j]))
                        if j > 0:
                            cur = max(cur, int(DP[k - 1][i][j - 1]))
                        if i < n - 1:
                            cur = max(cur, int(DP[k - 1][i + 1][j]))
                        if j < m - 1:
                            cur = max(cur, int(DP[k - 1][i][j + 1]))
                        DP[k][i][j] = max(cur, DP[k - 1][i][j])
        res = []
        print(DP)
        for i in range(n):
            c = []
            for j in range(m):
                c.append(DP[A][i][j])
            res.append(c)

        return res


if __name__ == '__main__':
    M = [[1, 2, 4], [4, 5, 8]]
    K = 2
    print(Solution().solve(K, M))

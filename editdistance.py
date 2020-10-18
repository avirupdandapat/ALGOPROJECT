class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def minDistance(self, A, B):
        n = len(A)
        m = len(B)
        D = [[0] * (m + 1) for i in range(n + 1)]  # D[n][m]
        # D[i][j] = minD(A[:i], B[:j])
        for i in range(n + 1): D[i][0] = i
        for i in range(m + 1): D[0][i] = i
        #print(D)
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                replace = D[i - 1][j - 1] + int(A[i - 1] != B[j - 1])
                insert = D[i][j - 1] + 1
                delete = D[i - 1][j] + 1
                D[i][j] = min(replace, insert, delete)
        print(D)
        return D[n][m]


if __name__ == '__main__':
    A = "Anshuman"
    B = "Antihuman"
    print(Solution().minDistance(A, B))

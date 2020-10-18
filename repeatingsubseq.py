class Solution:
    # @param A : string
    # @return an integer
    def anytwo(self, A):
        n = len(A)
        l = [[0 for x in range(n + 1)] for x in range(n + 1)]
        for i in range(n + 1):
            for j in range(n + 1):
                if i > 0 and j > 0:
                    if A[i - 1] == A[j - 1] and i != j:
                        l[i][j] = 1 + l[i - 1][j - 1]
                    else:
                        l[i][j] = max(l[i - 1][j], l[i][j - 1])
        if l[n][n] >= 2:
            return 1
        else:
            return 0


if __name__ == '__main__':
    A = "abaaba"
    print(Solution().anytwo(A))

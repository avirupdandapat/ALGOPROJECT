class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        l = len(A[0])
        if l == 0:
            return 0
        final = []
        sol = []
        for d in range((2 * (l - 1)) + 1):
            for i in range(d + 1):
                j = d - i
                if j >= l or i >= l:
                    pass
                else:
                    final.append(A[i][j])
                    print(d, i, j)
                    print(final)
                sol.append(final)
                final = []
        return sol


if __name__ == "__main__":
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(Solution().diagonal(A))

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def uniquePaths(self, A, B):
        def unpt(c, d):
            ans = 0
            ans = unpt(c - 1, d) + unpt(c, d - 1)
            return ans

        if A == 1 or B == 1:
            return 1
        else:
            return unpt(A, B)


if __name__ == '__main__':
    print(Solution().uniquePaths(2, 2))

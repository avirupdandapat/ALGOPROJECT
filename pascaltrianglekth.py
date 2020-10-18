class Solution:
    # @param A : integer
    # @return a list of list of integers
    def getRow(self, A):
        A += 1
        if A <= 0:
            return []
        result = [[1]]
        for r in range(1, A):
            row = [1]
            for i in range(1, r):
                row.append(result[r - 1][i - 1] + result[r - 1][i])
            row.append(1)
            result.append(row)
        return result[A-1]


if __name__ == "__main__":
    A = 2
    print(Solution().getRow(A))

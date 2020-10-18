class Solution:
    # @param A : integer
    # @return a list of list of integers
    def solve(self, A):

        if A <= 0:
            return []
        result = [[1]]
        for r in range(1, A):
            row = [1]
            for i in range(1, r):
                row.append(result[r - 1][i - 1] + result[r - 1][i])
            row.append(1)
            result.append(row)
        return result


if __name__ == "__main__":
    A = 5
    print(Solution().solve(A))

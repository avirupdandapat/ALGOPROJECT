class Solution:
    # @param A : list of strings
    # @return a list of list of integers
    def queenAttack(self, A):
        dp = [[0 for i in range(len(A[0]))] for j in range(len(A))]
        directions = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if A[i][j] == '0':
                    continue
                for k in directions:
                    x, y = i + k[0], j + k[1]
                    while (0 <= x < len(A)) and (0 <= y < len(A[0])):
                        #dp[x][y] += 1
                        if A[x][y] == 1:
                            dp[i][j] += 1
                            break
                        x, y = x + k[0], y + k[1]
        return dp


if __name__ == '__main__':
    A = [[0, 1, 0], [1, 0, 0], [0, 0, 1]]
    print(Solution().queenAttack(A))

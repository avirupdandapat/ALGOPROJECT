class Solution:
    # @param A : list of list of integers
    # @return an integer
    def adjacent(self, A):
        dp = [0]*len(A[0])
        for i in range(len(A[0])):
            if i-2>=0:
                dp[i] = max(dp[i-2] + max(A[0][i],A[1][i]), dp[i-1])
            elif i-1>=0:
                dp[i] = max(max(A[0][i],A[1][i]), dp[i-1])
            else:
                dp[i] = max(A[0][i],A[1][i])
        return dp[-1]
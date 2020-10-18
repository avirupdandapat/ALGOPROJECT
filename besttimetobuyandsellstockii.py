class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        if not A:
            return 0

        buy = A[0]
        max_profits = 0

        for i in range(1, len(A)):
            if A[i] > A[i - 1]:
                max_profits += A[i] - buy
            buy = A[i]

        return max_profits

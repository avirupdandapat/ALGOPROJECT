class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        if not A:
            return 0
        maxP = 0
        curMin = A[0]
        for p in A:
            maxP = max(p-curMin, maxP)
            curMin = min(curMin, p)
        return maxP
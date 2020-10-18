class Solution:
    # @param A : tuple of integers
    # @return an integer
    def lis(self, A):
        max_ss = [0] * (max(A) + 1)
        for num in A:
            max_ss[num] = max(max(max_ss[:num]) + 1, max_ss[num])
        return max(max_ss)
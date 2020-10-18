class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def mice(self, A, B):
        A = sorted(A)
        B = sorted(B)
        t = 0
        for i in range(len(A)):
            t = max(abs(A[i]-B[i]),t)
        return t
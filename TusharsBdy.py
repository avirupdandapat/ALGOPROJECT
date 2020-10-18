class Solution:
    # @param R : integer
    # @param A : list of integers
    # @return a list of integers
    def solve(self, R, A):
        smallest = float('inf')
        k = 0
        for i in range(len(A)):
            if A[i] < smallest:
                smallest = A[i]
                k = i
        tolerance = R % smallest
        res = [k] * (R // smallest)
        i = 0
        j = 0
        while j < k and i < len(res):
            if A[j] - smallest <= tolerance:
                res[i] = j
                tolerance -= A[j] - smallest
                i += 1
            else:
                j += 1
        return res

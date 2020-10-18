class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def order(self, A, B):
        # A = Heights
        # B = Infronts
        if not A:
            return []
        N = len(A)
        indi = [i[0] for i in sorted(enumerate(A), key=lambda x:x[1])]
        A.sort()
        m = max(B)
        ans = []
        for i in range(N):
            j = N - i - 1
            ans.insert(B[indi[j]], A[j])
        return ans
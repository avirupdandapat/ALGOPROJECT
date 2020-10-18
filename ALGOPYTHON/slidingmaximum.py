class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def slidingMaximum(self, A, B):
        if len(A) < B:
            return A
        slide, res = [], []
        for i in range(B):
            slide.append(A[i])
        res.append(max(slide))
        for j in range(B, len(A)):
            slide.append(A[j])
            print(slide)
            slide.pop(0)
            print(slide)
            res.append(max(slide))

        return res


if __name__ == '__main__':
    A = [1, 3, -1, -3, 5, 3, 6, 7]
    print(Solution().slidingMaximum(A, 3))

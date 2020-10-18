class Solution:
    # @param A : list of integers
    # @return an integer
    def maxcoin(self, A):
        if len(A) == 0:
            return 0
        elif len(A) == 1:
            return A[0]
        A.sort(reverse=True)
        i = 0
        res = 0
        while i <= len(A)-1:
            res = res + A[i]
            i += 2
        return res


if __name__ == '__main__':
    A = [1, 2, 3, 4]
    print(Solution().maxcoin(A))

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        minnum = 1
        for a in A:
            for b in B:
                for c in C:
                    minnum = min(minnum, abs(max(a, b, c) - min(a, b, c)))

        return minnum


if __name__ == '__main__':
    A= [1, 4, 5, 8, 10]
    B= [6, 9, 15]
    C= [2, 3, 6, 6]
    print(Solution().solve(A, B, C))
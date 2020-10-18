class Solution:
    # @param A : list of integers
    # @return A after the sort
    def sortColors(self, A):
        B = [0, 0, 0]
        for i in A:
            B[i] += 1
        print(B)
        return [0] * B[0] + [1] * B[1] + [2] * B[2]


if __name__ == '__main__':
    A = [0, 1, 2, 0, 1, 2, 2, 1]
    print(Solution().sortColors(A))

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def paint(self, A, B, C):
        if A >= len(C):
            return max(C) * B
        else:
            return  max(C) * (len(C) // A) * B

        return 0


if __name__ == '__main__':
    A = 10
    B = 1
    C = [1, 8, 11, 3]
    print(Solution().paint(A, B, C))
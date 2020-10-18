class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):
        A = sorted(A)
        for i in range(0, len(A) - 1, 2):
            print(i)
            A[i], A[i + 1] = A[i + 1], A[i]
        return A


if __name__ == "__main__":
    A = [1, 2, 3, 4, 5, 6, 7, 8]
    print(Solution().wave(A))

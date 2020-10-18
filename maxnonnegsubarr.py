class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        n = len(A)
        maximum, ansi, ansj = 0, -1, -1
        curr, curri, currj = 0, 0, 0
        for i in range(0, n):
            curr = curr + A[i]
            if A[i] < 0:
                curr, curri = 0, i + 1
            elif curr > maximum or (curr == maximum and i - curri > ansj - ansi):
                maximum, ansi, ansj = curr, curri, i

        return A[ansi:ansj + 1]


if __name__ == "__main__":
    A = [1, 2, 5, -7, 2, 3]
    print(Solution().maxset(A))

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        left, right = 0, len(A)-1
        while left >= 0 and right < len(A):
            if A[right] - A[left] == B:
                return 1
            elif A[right] - A[left] > B:
                right -= 1
            else:
                left += 1

        return 0


if __name__ == '__main__':
    A = [1, 3, 5, 50, 100]
    print(Solution().diffPossible(A, 4))
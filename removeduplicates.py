class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        i, j = 1, 0
        while i < len(A):
            if A[i] != A[j]:
                A[j + 1] = A[i]
                j += 1

            i += 1
        del A[j + 1:]
        return len(A)


if __name__ == '__main__':
    A = [1, 1, 1, 2]
    print(Solution().removeDuplicates(A))

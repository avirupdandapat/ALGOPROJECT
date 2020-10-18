class Solution:
    # @param A : list of integers
    # @return an integer
    def removeElement(self, A, B):
        i, j = 0, 0
        while i < len(A):
            if A[i] != B:
                A[j] = A[i]
                j += 1

            i += 1
        del A[j:]
        print(A)
        return len(A)


if __name__ == '__main__':
    A = [1, 4, 1, 1, 2, 1, 3]
    print(Solution().removeElement(A , 1))

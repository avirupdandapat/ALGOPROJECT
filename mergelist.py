class Solution:
    # @param A : list of integers
    # @param B : list of integers
    def merge(self, A, B):
        i = 0
        j = 0
        while i < len(A) and j < len(B):
            while i < len(A) and A[i] < B[j]:
                i += 1
            print(A)
            A.insert(i, B[j])
            j += 1
            i += 1
        return " ".join([str(x) for x in A]) + " "


if __name__ == '__main__':
    A = [1, 5, 8]
    B = [6, 9]
    print(Solution().merge(A, B))

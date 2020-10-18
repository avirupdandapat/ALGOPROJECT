class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def books(self, A, B):
        if B == len(A):
            return max(A)
        else:
            C = int(len(A)/2) + 1
            minpage = 0
            for i in range(len(A) - C):
                if i != 0:
                    minpage = min(minpage, minpagebook)
                minpagebook = 0
                for j in range(i, i+C):
                    minpagebook += A[j]
                if i ==0:
                    minpage = minpagebook

        return minpage


if __name__ == '__main__':
    A = [5, 17, 100, 11]
    B = 4
    print(Solution().books(A, B))

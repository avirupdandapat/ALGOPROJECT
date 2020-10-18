class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort(reverse=False)
        for i in range(len(A)):
            if A[i] == len(A) - i - 1:
                c = 1
                break
            else:
                c = -1

        return c


if __name__ == "__main__":
    A = [1, 2, 4, 8, 5, 6, 7]
    print(Solution().solve(A))

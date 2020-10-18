class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def intersect(self, A, B):
        ans = []
        A_pointer = 0
        B_pointer = 0
        while A_pointer < len(A) and B_pointer < len(B):
            if A[A_pointer] == B[B_pointer]:
                ans.append(A[A_pointer])
                A_pointer += 1
                B_pointer += 1

            elif A[A_pointer] < B[B_pointer]:
                A_pointer += 1

            else:
                B_pointer += 1

        return ans


if __name__ == '__main__':
    A= [1, 2, 3, 3, 4, 5, 6]
    B= [3, 3, 5]
    print(Solution().intersect(A, B))
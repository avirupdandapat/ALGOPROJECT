class Solution:
    # @param A : list of integers
    # @return an integer
    def canJump(self, A):

        for i in range(len(A) - 1):
            curr = i
            while curr <= len(A) - 1:
                print(curr)
                if curr == len(A) - 1:
                    return 1
                val = A[curr]
                if val == 0:
                    break
                else:
                    curr += val
        return 0


if __name__ == '__main__':
    A = [ 10, 0, 1, 1, 0 ]
    print(Solution().canJump(A))

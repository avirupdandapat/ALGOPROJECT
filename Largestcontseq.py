class Solution:
    # @param A : list of integers
    # @return a list of integers
    def lszero(self, A):
        ans = []
        prev, curr = 0, 0
        for i in range(len(A)):
            res = A[i]
            for j in range(i+1, len(A)):
                res = res + A[j]
                curr= j-i
                if res == 0:
                    if curr > prev:
                        prev = curr
                        ans = A[i:j+1]

        return ans


if __name__ == '__main__':
    A = [1, 2, -2, 4, -4]
    print(Solution().lszero(A))

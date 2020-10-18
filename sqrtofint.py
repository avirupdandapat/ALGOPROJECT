import math

class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        if A <= 0:
            return 0
        else:
            return round(math.log(A, 2))


if __name__ == '__main__':
    print(Solution().sqrt(0))
    print(9 // 2)

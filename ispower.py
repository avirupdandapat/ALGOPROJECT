class Solution:
    # @param A : integer
    # @return an integer
    def isPower(self, A):
        from math import log, sqrt
        if A == 1:
            return 1

        for i in range(2, int(sqrt(A)) + 1):
            print(round(log(A, i), 5),  i)
            x = round(log(A, i), 5)
            if x % 1 == 0:
                return 1

        return 0


if __name__ == '__main__':
    print(Solution().isPower(32))

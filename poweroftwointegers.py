from math import floor


class Solution:
    # @param A : integer
    # @return an integer
    def isPower(self, A):
        if A < 4:
            return 0
        for i in range(1, round(A ** 0.5) + 1):
            for j in range(2, round(A ** 0.5) + 1):
                if i ** j  == A:
                    return 1
        return 0


if __name__ == '__main__':
    print(Solution().isPower(31))
    print(round(32 ** 0.5) + 1)

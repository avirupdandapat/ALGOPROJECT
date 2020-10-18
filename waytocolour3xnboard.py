class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        c3 = 24
        c2 = 12
        temp = 0
        for i in range(2, A + 1):
            temp = c3
            c3 = (11 * c3 + 10 * c2) % 1000000007
            c2 = (5 * temp + 7 * c2) % 1000000007

        return (c3 + c2) % 1000000007


if __name__ == '__main__':
    print(Solution().solve(2))

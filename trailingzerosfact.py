class Solution:
    # @param A : integer
    # @return an integer
    def trailingZeroes(self, A):
        # Zero is formed by 2*5.
        # No. of 2's always > No. of 5's in factorial of a number.
        # Therefore, counting the No. of 5's gives the number of trailing zeros
        # If A < 5 then its factorial doesn't have any trailing zeros
        if A < 5:
            return 0
        count = 0
        i = 5
        while A // i > 0:
            print(i)
            count += A // i
            i *= 5
        return count


if __name__ == '__main__':
    print(Solution().trailingZeroes(101))


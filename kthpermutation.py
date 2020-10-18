from math import factorial as fact
class Solution:
    # @param A : integer
    # @param B : integer
    # @return a strings
    def getPermutation(self, A, B):
        digits = [str(i) for i in range(1, A + 1)]
        return self.recurse(digits, B - 1)

    def recurse(self, digits, k):
        n = len(digits)
        if n == 1:
            return digits[0]

        di = int(k / fact(n - 1))
        k2 = int(k % fact(n - 1))
        d = digits[di]
        digits = digits[:di] + digits[di + 1:]
        print(d, digits, k2)
        return d + self.recurse(digits, k2)


if __name__ == '__main__':
    print(Solution().getPermutation(3, 4))
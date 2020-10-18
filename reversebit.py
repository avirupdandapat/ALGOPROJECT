class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
        def intobinary(c):
            B = ''
            if c <= 0:
                return 0
            while c >= 1:
                B = B + str(c % 2)
                c = c // 2
            return B[::-1]
        n = A
        rn, cnt = 0, 0
        while cnt < 32:
            print('print1',intobinary(rn))
            rn <<= 1
            print('print2',intobinary(rn))
            print('print n', intobinary(n))
            rn |= (n & 1)
            print('print3', intobinary(rn))
            n >>= 1
            print('print4', intobinary(n))
            cnt += 1
        return rn


if __name__ == '__main__':
    print(Solution().reverse(11))

    print(11 >> 1)
class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        def intobinary(c):
            B = ''
            if c <= 0:
                return 0
            while c >= 1:
                B = B + str(c % 2)
                c = c // 2
            return B[::-1]
        intb = intobinary(A)
        print(intb)
        cn = 0
        for i in intb:
            if i == '1':
                cn += 1

        return cn


if __name__ == '__main__':
    print(Solution().numSetBits(11))

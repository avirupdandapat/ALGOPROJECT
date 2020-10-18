class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def divide(self, divident, divisor):
        sign = -1 if ((divident < 0) ^ (divisor < 0)) else 1

        divident = abs(divident)
        divisor = abs(divisor)

        temp = 0
        quotient = 0

        for idx in range(31, -1, -1):
            print('printloop1', idx, temp, (divisor << idx))
            if (temp + (divisor << idx)) <= divident:
                print('printloop2', idx, temp, (divisor << idx))
                temp += (divisor << idx)
                quotient |= (1 << idx)
                print('printloop3', quotient)

        quotient *= sign
        if quotient > (2 ** 31 - 1):
            return 2 ** 31 - 1
        elif quotient < -2 ** 31:
            return -2 ** 31
        else:
            return quotient


if __name__ == '__main__':
    print(Solution().divide(10000, 29))


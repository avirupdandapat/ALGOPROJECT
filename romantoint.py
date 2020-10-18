class Solution:
    # @param A : string
    # @return an integer
    def romanToInt(self, A):
        # XI - 9
        # IV

        bank = {'X': 10, 'V': 5, 'I': 1, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        res = 0
        for i in range(0, len(A)):
            cur = bank[A[i]]
            print(cur)
            if i + 1 < len(A) and cur < bank[A[i + 1]]:
                print('in')
                res -= cur
            else:
                res += cur

        return res


if __name__ == '__main__':
    print(Solution().romanToInt('LIVXV'))
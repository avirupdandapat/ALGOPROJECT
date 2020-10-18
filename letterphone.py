class Solution:
    # @param A : string
    # @return a list of strings
    def letterCombinations(self, A):
        def letters(l):
            if l == 2:
                return ['a', 'b', 'c']
            elif l == 3:
                return ['d', 'e', 'f']
            elif l == 4:
                return ['g', 'h', 'i']
            elif l == 5:
                return ['j', 'k', 'l']
            elif l == 6:
                return ['m', 'n', 'o']
            elif l == 7:
                return ['p', 'q', 'r', 's']
            elif l == 8:
                return ['t', 'u', 'v']
            elif l == 9:
                return ['w', 'x', 'y', 'z']

        def comb(l1, l2):
            res = []
            for l in l2:
                res.append(l1 + l)
            return res

        ans = letters(int(A[0]))
        output = []
        for i in range(1, len(A)):
            currnum = letters(int(A[i]))

            res = []
            for n in ans:
                res.append(comb(n, currnum))
            ans = []
            ans = res

        return ans


if __name__ == '__main__':
    print(Solution().letterCombinations('23'))

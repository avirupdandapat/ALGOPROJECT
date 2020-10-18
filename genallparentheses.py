class Solution:
    def genParanth(self, open, closed, n, s):
        if closed == n:
            return [s]
        res = []
        if open < n:
            res += self.genParanth(open + 1, closed, n, s + '(')
        if open > closed:
            res += self.genParanth(open, closed + 1, n, s + ')')
        return res

    # @param A : integer
    # @return a list of strings
    def generateParenthesis(self, A):
        return self.genParanth(0, 0, A, '')


if __name__ == '__main__':
    print(Solution().generateParenthesis(3))

class Solution:
    # @param A : string
    # @return a list of strings

    d2l = {0: '0',
           1: '1',
           2: 'abc',
           3: 'def',
           4: 'ghi',
           5: 'jkl',
           6: 'mno',
           7: 'pqrs',
           8: 'tuv',
           9: 'wxyz'}

    def letterCombinations(self, A):
        if len(A) == 0: return ['']
        return [letter + s for letter in Solution.d2l[int(A[0])] for s in self.letterCombinations(A[1:])]


if __name__ == '__main__':
    print(Solution().letterCombinations('23'))
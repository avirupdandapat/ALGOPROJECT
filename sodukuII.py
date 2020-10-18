class Solution:
    # @param A : tuple of strings
    # @return an integer
    def isValidSudoku(self, A):
        for i in range(9):
            if not self.isValidArray(list(A[i])) \
                    or not self.isValidArray([A[j][i] for j in range(9)]) \
                    or not self.isValidArray([A[3 * (i // 3) + j // 3][3 * (i % 3) + j % 3] for j in range(9)]):
                return 0
        return 1

    def isValidArray(self, arr):
        s = set()
        for x in arr:
            if x in s:
                return False
            if x != '.':
                s.add(x)
        return True


if __name__ == '__main__':
    A = [['5', '3', '.', '.', '7', '.', '.', '.', '.'], ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
         ['.', '9', '8', '.', '.', '.', '.', '6', '.'], ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
         ['4', '.', '.', '8', '.', '3', '.', '.', '1'], ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
         ['.', '6', '.', '.', '.', '.', '2', '8', '.'], ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
         ['.', '.', '.', '.', '8', '.', '.', '7', '9']]
    print(Solution().isValidSudoku(A))
    i = 0
    res = [A[3 * (i // 3) + j // 3][3 * (i % 3) + j % 3] for j in range(9)]
    print(res)


class Solution:
    # @param A : string
    # @return an integer
    def isNumber(self, A):
        try:
            a = float(A)
            for i in range(len(A)):
                if A[i] == '.' and i != len(A)-1:
                    if int(A[i+1]) in range(0, 10):
                        pass
                    else:
                        return 1
            if A[len(A)-1] == '.':
                return 0
            else:
                return 1
        except ValueError:
            return 0


if __name__ == '__main__':
    print(Solution().isNumber('2.7'))
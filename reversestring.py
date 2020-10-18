class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        B = ''
        A = (str.split(A, ' ')[::-1])
        for i in range(len(A)):
            if i == 0:
                B = B + str(A[i])
            else:
                B = B + ' ' + str(A[i])
        return  B

if __name__ == '__main__':
    print(Solution().solve('Hello World'))

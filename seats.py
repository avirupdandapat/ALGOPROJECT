class Solution:

    # @param A : string
    # @return an integer
    def seats(self, A):
        n = len(A)
        peoples = 0
        start, end = n, 0
        for i in range(n):
            if A[i] == 'x':
                start = min(start, i)
                end = max(end, i)
                peoples += 1

        left = 0
        jumps = 0
        for i in range(start, end + 1):
            if A[i] == 'x':
                left += 1
            else:
                jumps += min(left, peoples - left)

        return jumps % 10000003
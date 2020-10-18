from heapq import *


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def dNums(self, A, B):
        if B > len(A):
            return []
        res = []
        for i in range(0, len(A) - B+1):
            ct = set()
            for j in range(i, B+i):
                ct.add(A[j])
            res.append(len(ct))

        return res


if __name__ == '__main__':
    A = [1, 2, 1, 3, 4, 3]
    B = 3
    print(Solution().dNums(A, B))

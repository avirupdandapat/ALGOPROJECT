import math
import statistics

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def findMedian(self, A):
        B = []
        for i in A:
            for j in i:
                B.append(j)

        return statistics.median(B)


if __name__ == '__main__':
    A = [[1, 3, 5],
         [2, 6, 9],
         [3, 6, 9]]
    print(Solution().findMedian(A))

from heapq import *


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        h = []
        A.sort(reverse=True)
        B.sort(reverse=True)
        heappush(h, (-1 * (A[0] + B[0]), 0, 0))
        print(A, B, h)
        ans = []
        k = len(B)
        m = set()
        m.add((0, 0))
        while k > 0:
            u, i, j = heappop(h)
            print(h, u, i, j)
            ans.append(-1 * u)
            k -= 1
            if i < len(A) - 1 and (i + 1, j) not in m:
                heappush(h, ((-1 * (A[i + 1] + B[j])), i + 1, j))
                m.add((i + 1, j))
            if j < len(B) - 1 and (i, j + 1) not in m:
                heappush(h, ((-1 * (A[i] + B[j + 1])), i, j + 1))
                m.add((i, j + 1))
        return ans


if __name__ == '__main__':
    A = [1, 4, 2, 3]
    B = [2, 5, 1, 6]
    N = 4
    print(Solution().solve(A, B))

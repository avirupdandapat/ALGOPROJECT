from _collections import deque


class Solution:
    # @param A : list of strings
    # @return an integer

    def black(self, A):
        def neighbour(A, lst, i, j):
            lst.remove((i,j))
            moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]
            q = deque()
            q.append((i, j))
            while q:
                ls = q.popleft()
                for r in moves:
                    m = ls[0] + r[0]
                    n = ls[1] + r[1]
                    if A[m][n] == 1:
                        if (m,n) not in lst:
                            lst.append((m, n))
                        q.append((m, n))

            print(lst)
            return lst

        res = 0
        lst = []
        for i in range(len(A)):
            for j in range(len(A[i])):
                if A[i][j] == 1:
                    #print(lst)
                    if (i,j) not in lst:
                        lst.append((i, j))
                        #print(i,j,res)
                        res += 1
                        lst = neighbour(A, lst, i, j)
                        #print(lst)
                    else:
                        continue

        return res


if __name__ == '__main__':
    A = [[0, 0, 0, 1, 0, 0, 0],
         [0, 0, 1, 1, 0, 1, 0],
         [0, 1, 0, 0, 0, 1, 0]]
    print(Solution().black(A))

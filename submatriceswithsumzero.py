class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        if len(A) == 0:
            return 0
        N = len(A)
        M = len(A[0])
        sol = 0
        for i in range(N):
            pre_sum = [0 for x in range(M)]
            for j in range(i, N):
                for k in range(M):
                    pre_sum[k] += A[j][k]
                number_count = {0: 1}
                cur_sum = 0
                for k in range(M):
                    cur_sum += pre_sum[k]
                    if cur_sum not in number_count:
                        number_count[cur_sum] = 0
                    sol += number_count[cur_sum]
                    number_count[cur_sum] += 1
        return sol

if __name__ == '__main__':
    A = [[-8, 5, 7], [3, 7, -8], [5, -8, 9]]
    print(Solution().solve(A))
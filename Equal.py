class Solution:
    # @param A : list of integers
    # @return a list of integers
    def equal(self, A):
        seen = dict()
        result = set()
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                curr_sum = A[i] + A[j]
                if curr_sum in seen :
                    for prev_sum in seen[curr_sum]:
                        if A[i] <= A[j] and prev_sum[0]< prev_sum[1] < i < j:
                            result.add((prev_sum[0], prev_sum[1], i, j))
                    seen[curr_sum].append((i, j))
                else:
                    seen[curr_sum] = [(i, j)]

        return list(result.pop())


if __name__ == '__main__':
    A = [3, 4, 7, 1, 2, 9, 8]
    print(Solution().equal(A))

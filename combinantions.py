class Solution:
    # @param A : integer
    # @param B : integer
    # @return a list of list of integers
    def combine(self, A, B):
        res = []
        for i in range(1, A):
            for j in range(i+1, A+1):
                res.append([i, j])

        return res


if __name__ == '__main__':
    print(Solution().combine(4, 2))
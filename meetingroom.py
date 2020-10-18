class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        if len(A) == 0:
            return 0
        start, end = [], []
        for i in A:
            start.append(i[0])
            end.append(i[1])
        start.sort()
        end.sort()
        idx = 0
        for i in range(len(start)):
            if start[i] > end[idx]:
                idx += 1

        return len(end) - idx


if __name__ == "__main__":
    A = [[0, 30],
         [5, 10],
         [15, 20]
         ]
    print(Solution().solve(A))

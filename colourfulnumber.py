class Solution:
    # @param A : integer
    # @return an integer
    def colorful(self, A):
        N = str(A)
        vals = set()
        for l in range(1, len(N) + 1):
            for i in range(0, len(N) - l + 1):
                ans = 1
                for k in range(i, i + l):
                    print(l, i, k)
                    ans *= int(N[k])
                #if ans in vals:
                    #return 0
                vals.add(ans)
        return 1


if __name__ == '__main__':
    print(Solution().colorful(236))

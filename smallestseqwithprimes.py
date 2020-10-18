class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @return a list of integers
    def solve(self, A, B, C, D):
        dic = {}
        ans = []
        dic[A] = dic[B] = dic[C] = 1
        for i in range(D):
            val = min(dic)
            ans.append(val)
            del dic[val]
            dic[val * A] = dic[val * B] = dic[val * C] = 1
        return ans


if __name__ == '__main__':
    A = 2
    B = 3
    C = 5
    D = 5
    print(Solution().solve(A, B, C, D))

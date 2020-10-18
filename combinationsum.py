def fun(A, ans, final, index, k):
    if k < 0:
        return
    if k == 0:
        a = final[:]
        if a not in ans:
            ans.append(a)
        return
    for i in range(index, len(A)):
        final.append(A[i])
        fun(A, ans, final, i, k - A[i])
        final.pop()
    return ans


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum(self, A, B):
        A.sort()
        return fun(A, [], [], 0, B)


if __name__ == '__main__':
    A = [10,1,2,7,6,1,5]
    print(Solution().combinationSum(A, 8))

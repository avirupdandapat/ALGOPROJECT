def fun(A, ans, final, index):
    a = final[:]
    print(a)
    if a not in ans:
        ans.append(a)
    for i in range(index, len(A)):
        final.append(A[i])
        fun(A, ans, final, i + 1)
        final.pop()
    return ans


class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsetsWithDup(self, A):
        A.sort()
        return fun(A, [], [], 0)


if __name__ == '__main__':
    A = [1, 2, 2]
    print(Solution().subsetsWithDup(A))

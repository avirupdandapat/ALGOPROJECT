def fun(a, size, n, ans):
    # if size becomes 1 then prints the obtained
    # permutation
    if size == 1:
        b = a[:]  # deep copy
        ans.append(b)
        return

    for i in range(size):
        fun(a, size - 1, n, ans);

        # if size is odd, swap first and last
        # element
        # else If size is even, swap ith and last element
        if size % 2 == 1:
            a[0], a[size - 1] = a[size - 1], a[0]
        else:
            a[i], a[size - 1] = a[size - 1], a[i]

    return ans


class Solution:
    # @param A : list of integers
    # @return a list of list of integers

    def permute(self, A):
        if len(A) == 1:
            return [[1]]
        res = fun(A, len(A), len(A), [])
        return res


if __name__ == '__main__':
    A = [1, 2, 3]
    print(Solution().permute(A))

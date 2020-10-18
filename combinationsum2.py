class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum(self, A, B):
        A.sort()
        ans = set()

        def combinationSumHelper(arr, sumSoFar, index):
            if sumSoFar == B:
                ans.add(tuple(arr))
            elif sumSoFar > B:
                return
            else:
                for i in range(index, len(A)):
                    combinationSumHelper(arr + [A[i]], sumSoFar + A[i], i + 1)

        combinationSumHelper([], 0, 0)

        return list(ans)


if __name__ == '__main__':
    A = [10, 1, 2, 7, 6, 1, 5]
    print(Solution().combinationSum(A, 8))

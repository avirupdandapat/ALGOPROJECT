class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def twoSum(self, A, B):
        d = {}
        A = list(A)
        for i in range(len(A)):
            t = B - A[i]
            if t in d:
                # l = d[t]
                # r = i+1
                return d[t], i + 1
            else:
                if A[i] not in d:
                    d[A[i]] = i + 1
        return ()


if __name__ == '__main__':
    A = [1, 2, -2, 4, -4, 5, -5]
    print(Solution().twoSum(A, 9))
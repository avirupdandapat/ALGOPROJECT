class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
        A.sort()
        print(A)
        n = len(A)
        res = float('inf')
        for i in range(0, n - 2):
            left = i + 1
            right = n - 1
            while left < right:
                s = A[i] + A[left] + A[right]
                print(A[i], A[left], A[right], res, B, s)
                if abs(res - B) > abs(s - B):
                    res = s
                if s == B:
                    return B
                if s > B:
                    right -= 1
                else:
                    left += 1
        return res


if __name__ == '__main__':
    A = [-1, 2, 1, -4, 10, 20]
    print(Solution().threeSumClosest(A, 1))

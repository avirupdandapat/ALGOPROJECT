class Solution:
    # @param A : list of integers
    # @return an integer
    def nTriang(self, A):
        A.sort(reverse=True)
        t = 0
        # Logic: Sum of 2 sides > third side.
        for i in range(0, len(A) - 2):
            third_side = A[i]
            if third_side == 0:
                break
            j = i + 1
            k = len(A) - 1
            while j < k:
                if A[j] + A[k] > third_side:
                    t += (k - j)
                    j += 1
                else:
                    k -= 1
        return t % (10**9 + 7)


if __name__ == '__main__':
    A = [1, 1, 1, 2, 2]
    print(Solution().nTriang(A))
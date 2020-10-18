class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestSubsequenceLength(self, a):
        l = len(a)
        inc = [1] * l
        dec = [1] * l
        for i in range(1, l):
            for j in range(i):
                if a[j] < a[i] and inc[i] < inc[j] + 1:
                    inc[i] = inc[j] + 1
        for i in range(l - 2, -1, -1):
            for j in range(l - 1, i, -1):
                if a[j] < a[i] and dec[i] < dec[j] + 1:
                    dec[i] = dec[j] + 1
        ans = 0
        for i in range(l):
            ans = max(ans, inc[i] + dec[i] - 1)
        return ans

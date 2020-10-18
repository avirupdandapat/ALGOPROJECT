class Solution:
    # @param A : tuple of integers
    # @return an integer
    n = 0

    def findMin(self, A):
        cnt = self.findCnt(A)
        return A[cnt]

    def findCnt(self, A):
        if self.n != 0: return -1
        self.n += 1
        lo = 0
        l = len(A)
        hi = l - 1
        while lo <= hi:
            if A[lo] <= A[hi]:
                # print  "n0=",self.n
                return lo

            mid = lo + (hi - lo) // 2
            nex = (mid + 1) % l
            pre = (mid + l - 1) % l
            # print mid, nex,pre
            if A[mid] <= A[nex] and A[mid] <= A[pre]:
                return mid
            elif A[mid] <= A[hi]:
                hi = mid - 1
            elif A[mid] >= A[lo]:
                lo = mid + 1
        return -1

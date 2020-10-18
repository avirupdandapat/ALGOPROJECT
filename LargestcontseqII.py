class Solution:
    # @param A : list of integers
    # @return a list of integers
    def lszero(self, A):
        seen_sums = dict()
        sm = 0
        strt, end = 0,0
        seen_sums[0] = 0
        for idx, a in enumerate(A,1):
            sm += a
            print(idx, a, sm, seen_sums)
            if sm in seen_sums:
                print('in')
                if end-strt < idx - seen_sums[sm]:
                    strt, end = seen_sums[sm], idx
            else:
                seen_sums[sm] = idx

        return A[strt:end] if strt != end else []


if __name__ == '__main__':
    A = [1, 2, -2, 4, -4, 5, -5]
    print(Solution().lszero(A))
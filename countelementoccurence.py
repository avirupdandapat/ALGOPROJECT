class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def findCount(self, A, B):

        def serachpos(c, d, firstflag):
            low, high, mid, result = 0, len(A), 0, -1
            while low <= high:
                mid = int(high - (high - low) / 2)
                if A[mid] == B:
                    result = mid
                    if firstflag:
                        high = mid - 1
                    else:
                        low = mid + 1

                elif A[mid] > B:
                    high = mid - 1
                else:
                    low = mid + 1
            return result

        searchfirstpos = serachpos(A, B, True)
        if searchfirstpos == -1:
            return 0
        else:
            searchlastpos = serachpos(A, B, False)
            return searchlastpos-searchfirstpos+1


if __name__ == '__main__':
    A = [5, 7, 7, 8, 8, 8, 8, 10]
    B = 2
    print(Solution().findCount(A, B))

class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def minWindow(self, A, B):
        r = dict()
        res = []
        for i in B:
            r[i] = 1

        for s in range(len(A)):
            str = ''
            r2 = dict(r)
            if A[s] in r2:
                str = str + A[s]
                del r2[A[s]]
                j = s
                while j < len(A) - 1:
                    j += 1
                    if len(r2) == 0:
                        break
                    elif len(r2) > 0:
                        if A[j] in r2:
                            del r2[A[j]]
                        str = str + A[j]
                if len(r2) == 0:
                    res.append(str)
        result = ''
        currlen, minlen = 0, 0
        for i in range(len(res)):
            currlen = len(res[i])
            if i == 0:
                minlen = currlen
            else:
                minlen = min(minlen, currlen)
            if minlen == currlen:
                result = res[i]
        return result


if __name__ == '__main__':
    print(Solution().minWindow('SADOBECODEBANC', 'ABC'))

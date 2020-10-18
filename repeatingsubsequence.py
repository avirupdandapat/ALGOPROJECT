def isInter(A, B, C, cache):
    if len(A) == 0 and len(B) == 0 and len(C) == 0:
        return True

    key = (len(A), len(B), len(C))
    if key in cache:
        return cache[key]
    r = False

    if len(A) > 0 and len(C) > 0 and A[0] == C[0]:
        r |= isInter(A[1:], B, C[1:], cache)

    if len(B) > 0 and len(C) > 0 and B[0] == C[0]:
        r |= isInter(A, B[1:], C[1:], cache)

    cache[key] = r
    return r


class Solution:
    # @param A : string
    # @param B : string
    # @param C : string
    # @return an integer
    def isInterleave(self, A, B, C):
        if isInter(A, B, C, {}):
            return 1
        return 0
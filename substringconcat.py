class Solution:
    # @param A : string
    # @param B : tuple of strings
    # @return a list of integers
    def findSubstring(self, A, B):
        n = len(A)
        m = len(B)
        l = len(B[0])

        S = {b: 0 for b in B}
        for b in B:
            S[b] += 1
        print(S)

        Ind = []
        ct = 0
        i = 0
        while i < n - l * m + 1:
            if A[i:i + l] not in S:
                i += 1
                continue
            tempS = {i: 0 for i in S}
            j = i
            while A[j:j + l] in tempS and tempS[A[j:j + l]] < S[A[j:j + l]]:
                tempS[A[j:j + l]] += 1
                j += l
                ct += 1
                if ct == m:
                    Ind.append(i)
                    break
            ct = 0
            i += 1

        return Ind


if __name__ == '__main__':
    A = "footbarfoobar"
    B = ["foo", "bar"]
    print(Solution().findSubstring(A, B))
class Solution:
    # @param A : string
    # @param B : integer
    # @return a strings
    def convert(self, A, B):
        if B == 1:
            return A
        C = []
        cn, i, zig = 0, 0, 'down'
        print(len(A) - 1)
        while cn < len(A):
            C.append([i, A[cn]])
            if zig == 'down':
                i += 1
            elif zig == 'up':
                i -= 1
            if i == B - 1:
                zig = 'up'
            elif i == 0:
                zig = 'down'
            cn += 1
        res = ''
        for i in range(B):
            dn = 0
            while dn <= len(C) - 1:
                if i == C[dn][0]:
                    res = res + str(C[dn][1])
                dn += 1

        return res


if __name__ == '__main__':
    print(Solution().convert('PAYPALISHIRING', 3))
    

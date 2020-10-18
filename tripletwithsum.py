class Solution:
    # @param A : list of strings
    # @return an integer
    def solve(self, A):
        n = len(A)
        a = float(A[0])
        b = float(A[1])
        c = float(A[2])
        for i in range(3, n):
            if 1 < (a + b + c) < 2:
                return 1
            elif (a + b + c) > 2:
                if a > b and a > c:
                    a = float(A[i])
                elif b > a and b > c:
                    b = float(A[i])
                elif c > a and c > b:
                    c = float(A[i])
            else:
                if a < b and a < c:
                    a = float(A[i])
                elif b < a and b < c:
                    b = float(A[i])
                elif c < a and c < b:
                    c = float(A[i])
        if 1 < (a + b + c) < 2:
            return 1
        else:
            return 0


if __name__ == "__main__":
    A = [1.6, 0.7, 0.8, 1.2, 0.5]
    print(Solution().solve(A))

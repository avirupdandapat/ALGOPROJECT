class Solution:
    # @param A : integer
    # @return an integer
    def chordCnt(self, A):
        if A == 0 or A == 1:
            return 1

        # Table to store results of subproblems
        catalan = [0 for i in range(A + 1)]

        # Initialize first two values in table
        catalan[0] = 1
        catalan[1] = 1

        # Fill entries in catalan[] using recursive formula
        for i in range(2, A + 1):
            catalan[i] = 0
            for j in range(i):
                catalan[i] = catalan[i] + catalan[j] * catalan[i - j - 1]

        # Return last entry
        return catalan[A] % 1000000007

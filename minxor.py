class Solution:
    # @param A : list of integers
    # @return an integer
    def findMinXor(self, seq):
        seq.sort()
        min_xor = seq[0] ^ seq[1]
        # min is always achieved by two neighbours in sorted array
        for i in range(len(seq) - 1):
            min_xor = min(min_xor, seq[i] ^ seq[i + 1])
        return min_xor


if __name__ == '__main__':
    A = [0, 2, 5, 7]
    print(Solution().findMinXor(A))

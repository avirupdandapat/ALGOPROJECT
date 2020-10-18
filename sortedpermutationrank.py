# rank = number of characters less than first character * (N-1)! + rank of permutation of string with the first character removed
class Solution:
    def findRankUtil(self, A, i):
        rank = self.pos[A[i]] + 1
        if i + 1 < len(A):
            rank = self.pos[A[i]] * self.fact[len(A) - 1 - i]
            for ch in self.pos:
                if ch > A[i]:
                    self.pos[ch] -= 1
            rank += self.findRankUtil(A, i + 1)
        return rank

    # @param A : string
    # @return an integer
    def findRank(self, A):
        self.pos = {}
        self.fact = [1]
        B = sorted(list(A))
        for i in range(len(B)):
            self.pos[B[i]] = i
            self.fact.append(self.fact[-1] * (i + 1))
        print(self.fact, self.pos)
        return self.findRankUtil(A, 0) % 1000003


if __name__ == '__main__':
    print(Solution().findRank('view'))
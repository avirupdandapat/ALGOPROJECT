class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLongestSubstring(self, A):
        if len(A) == 1:
            return 1
        res = dict()
        str = ''
        ln = 0

        for i in A:
            if i not in res:
                str = str + i
                res[i] = 1
            else:
                ln = max(ln, int(len(str)))
                str = ''
                res[i] = 1

        return ln


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring('abcabcbb'))

class Solution:
    # @param A : integer
    # @return an integer
    def isPalindrome(self, A):
        ln = len(str(A))
        for i in range(round(len(str(A))/2)):
            if str(A)[i] != str(A)[ln - i - 1]:
                return 0
        return 1


if __name__ == '__main__':
    print(Solution().isPalindrome(12120))

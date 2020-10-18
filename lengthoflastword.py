class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        print(len((str.split(A, ' ')[len(str.split(A, ' ')) - 1])))


if __name__ == '__main__':
    print(Solution().lengthOfLastWord('Hello World'))
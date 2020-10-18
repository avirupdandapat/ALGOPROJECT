class Solution:
    # @param A : integer
    # @return a strings
    def convertToTitle(self, A):
        mydict = 'ZABCDEFGHIJKLMNOPQRSTUVWXY'

        s = ''
        while A > 0:
            aux = A % 26
            s = mydict[aux] + s
            A = A // 26
            if 0 == aux:
                A -= 1

        return s


if __name__ == '__main__':
    print(Solution().convertToTitle(532))

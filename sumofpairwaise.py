class Solution:
    # @param A : tuple of integers
    # @return an integer
    def hammingDistance(self, A):
        def findDigitsInBinary(A):
            if A == 0:
                return '0'
            l = []
            while A > 0:
                rem = A % 2
                l.append(str(rem))
                A = int(A / 2)

            return ''.join(l[::-1])

        def noOfDigits(A):
            count = 0
            while A > 0:
                count = count + 1
                A = A // 10
            return count

        dg = noOfDigits(max(c[0], c[1]))
        print(abs(noOfDigits(int(findDigitsInBinary(c[0]))) - noOfDigits(int(findDigitsInBinary(c[1])))))



if __name__ == "__main__":
    c = (2, 7)
    print(Solution().hammingDistance(c))

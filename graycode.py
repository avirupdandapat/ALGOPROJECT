class Solution:
    # input: length of binary words
    # output: list of integers in gray code
    def grayCode(self, n):
        gray_seq = [0, 1]  # gray code for n=1
        for i in range(1, n):  # recursively extending for n>1
            print(i, gray_seq)
            gray_seq += [s + 2 ** i for s in reversed(gray_seq)]

        return gray_seq


if __name__ == '__main__':
    print(Solution().grayCode(3))
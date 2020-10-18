class Solution:
    # @param A : string
    # @return an integer
    def numDecodings(self, s):
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        print(dp)
        for i in range(1, len(dp)):
            if s[i - 1] != '0':
                dp[i] = dp[i - 1]

            if i != 1 and '10' <= s[i - 2: i] <= '26':
                dp[i] += dp[i - 2]

        print(dp)
        return dp[-1]


if __name__ == '__main__':
    print(Solution().numDecodings('12'))
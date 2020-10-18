class Solution:
    # @param A : string
    # @param B : integer
    # @return an integer
    def arrange(self, A, B):
        self.memo = {}
        if B > len(A):
            return -1
        return self.helper(0, A, len(A), B)

    def helper(self, curr_index, horses, len_horses, k):
        memo_str = "k" + str(k) + "i" + str(curr_index)
        if memo_str in self.memo:
            return self.memo[memo_str]

        ans = 999999999
        curr_ans = 0
        curr_w = 0
        curr_b = 0

        if k == 1:
            for i in range(curr_index, len_horses):
                if horses[i] == 'W':
                    curr_w += 1
                else:
                    curr_b += 1
            self.memo[memo_str] = curr_b * curr_w
            return curr_b * curr_w

        for i in range(curr_index, len_horses - k + 1):
            if horses[i] == 'W':
                curr_w += 1
            else:
                curr_b += 1
            curr_ans = curr_b * curr_w
            curr_ans += self.helper(i + 1, horses, len_horses, k - 1)
            ans = min(ans, curr_ans)

        self.memo[memo_str] = ans
        return ans
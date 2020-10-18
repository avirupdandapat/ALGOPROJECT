class Solution:
    # @param s : string
    # @param p : string
    # @return an integer
    def isMatch(self, s, p):
        i = j = 0
        star_pos = None
        while i < len(s):
            if j < len(p):
                if s[i] == p[j] or p[j] == '?':
                    i, j = i + 1, j + 1
                    continue
                elif p[j] == '*':

                    star_pos = j
                    curr_state_start = i
                    j += 1
                    continue

            if star_pos is not None:
                i = curr_state_start + 1
                curr_state_start += 1
                j = star_pos + 1
            else:  # mismatch and no star also
                return False

        while j < len(p) and p[j] == '*':
            j += 1
        return j == len(p) and i == len(s)


if __name__ == '__main__':
    A = "ab"
    B = "?*"
    print(Solution().isMatch(A, B))
class Solution:
    # @param A : string
    # @return a list of strings
    def isvalid(self, s):
        s = s.split(".")
        for i in s:
            if len(i) > 3 or int(i) < 0 or int(i) > 255:
                return False
            if len(i) > 1 and int(i) == 0:  # for i=000 or i=00
                return False
            if len(i) > 1 and int(i) > 0 and i[0] == "0":
                return False
        return True

    def restoreIpAddresses(self, A):
        n = len(A)
        if n > 12 or n < 4:
            return []
        l = []
        s = A
        # loop for inserting 3 "." in the string.
        for i in range(1, n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    s = s[:i] + "." + s[i:]
                    s = s[:j + 1] + "." + s[j + 1:]  # j+1 to account for 1 extra "."
                    s = s[:k + 2] + "." + s[k + 2:]  # k+2 to account for 2 extra "."
                    print(s)
                    if self.isvalid(s):
                        l.append(s)
                    s = A
        return l


if __name__ == '__main__':
    print(Solution().restoreIpAddresses('25525511135'))
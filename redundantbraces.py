class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
        stack = []
        for char in A:
            if char == ')':
                top = stack.pop()
                flag = 1
                while top != '(':
                    if top in ['+', '*', '/', '-']:
                        flag = 0
                    top = stack.pop()
                if flag == 1:
                    return 1
            else:
                stack.append(char)

        return 0


if __name__ == '__main__':
    print(Solution().braces('(a + (a + b))'))
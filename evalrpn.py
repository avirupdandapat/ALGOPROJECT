class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):
        if len(A) <= 1:
            return A
        res = 0
        stack = []
        for i in range(len(A)):
            if A[i] == "+" or A[i] == "-" or A[i] == "*" or A[i] == "/":
                numb1 = int(stack.pop())
                numb2 = int(stack.pop())
                if A[i] == '+':
                    res = numb2 + numb1
                elif A[i] == '-':
                    res = numb2 - numb1
                elif A[i] == '*':
                    res = numb2 * numb1
                elif A[i] == '/':
                    res = numb2 / numb1
                stack.append(res)
            else:
                stack.append(A[i])

        return res


if __name__ == '__main__':
    A = ["4", "13", "5", "/", "+"]
    print(Solution().evalRPN(A))

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def prevSmaller(self, A):
        stack, G = [], []
        for i in range(len(A)):
            if len(stack) < 1:
                stack.append(A[i])
                G.append(-1)
            elif A[i] > A[i-1]:
                G.append(A[i-1])
            elif stack[0] > A[i]:
                G.append(-1)
                stack.pop()
                stack.append(A[i])

            else:
                G.append(stack[0])

        return G


if __name__ == '__main__':
    A = [ 34, 35, 27, 42, 5, 28, 39, 20, 28 ]
    print(Solution().prevSmaller(A))
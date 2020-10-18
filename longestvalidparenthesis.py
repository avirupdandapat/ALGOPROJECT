class Solution:
    # @param A : string
    # @return an integer
    def longestValidParentheses(self, A):
        ## stack to store unbalanced parenthesis indexes
        ## -1 at starting and len(A) is added at end to cover corner cases like full balanced parenthesis etc.
        stack = [-1]
        for x in range(len(A)):

            ## if next element is "(" push its indexes in stack
            if A[x] == "(":
                stack.append(x)

            ## if next element is ")"
            else:
                ## then check if last elemet in stack is "(" pop it
                if len(stack) > 1 and A[stack[-1]] == "(":
                    stack.pop()

                ## else push its indexes
                else:
                    stack.append(x)

        ## len(A) is added as mentioned above to take care of corner cases
        stack.append(len(A))

        ## gap between adjacent unbalanced parenthesis indexes = length of balanced parenthesis in between
        maxGap = 0
        for x in range(1, len(stack)):
            maxGap = max(stack[x] - stack[x - 1] - 1, maxGap)

        ## return maxGap
        return maxGap

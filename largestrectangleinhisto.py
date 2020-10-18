class Solution:
    # @param A : list of integers
    # @return an integer
    def largestRectangleArea(self, A):
        def nearestSmaller(arr, flag=False):

            n = len(arr)
            result = []
            stack = []

            # Initialization for nearest common to right
            pseudoIndex = n
            start = n - 1
            stop = -1
            step = -1

            # Change initialization for nearest common to right
            if flag:
                pseudoIndex = -1
                start = 0
                stop = n
                step = +1

            for i in range(start, stop, step):
                if len(stack) == 0:
                    result.append(pseudoIndex)
                elif stack[-1][0] < arr[i]:
                    result.append(stack[-1][1])
                else:
                    while len(stack) > 0 and stack[-1][0] >= arr[i]:
                        stack.pop()
                    if len(stack) == 0:
                        result.append(pseudoIndex)
                    else:
                        result.append(stack[-1][1])
                stack.append((arr[i], i))

            return result

        right = nearestSmaller(A)[::-1]  # reverse to get correct order
        left = nearestSmaller(A, True)
        print(right)
        print(left)
        width = [right[i] - left[i] - 1 for i in range(len(A))]
        print(width)
        area = [width[i] * A[i] for i in range(len(A))]
        print(area)
        return max(area)

        return largestRectarea


if __name__ == '__main__':
    A = [90, 58, 69, 70, 82, 100, 13, 57, 47, 18]
    print(Solution().largestRectangleArea(A))


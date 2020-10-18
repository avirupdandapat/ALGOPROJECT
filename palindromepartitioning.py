def isPalind(string,
             low, high):
    while low < high:
        if string[low] != string[high]:
            return False
        low += 1
        high -= 1
    return True


def decompose(A, partialdecomposition, decompositions, workingindex ):
    if workingindex == len(A):
        a = partialdecomposition[:]
        decompositions.append(a)

    for i in range(workingindex, len(A)):
        if isPalind(A, workingindex, i):
            palindromicSnippet = A[workingindex:i + 1]
            partialdecomposition.append(palindromicSnippet)

            decompose(A, partialdecomposition, decompositions, i + 1)
            print('notpop',partialdecomposition)
            partialdecomposition.pop()
            print('pop',partialdecomposition)

    return decompositions


class Solution:
    # @param A : string
    # @return a list of list of strings
    def partition(self, A):
        return decompose(A, [], [], 0)


if __name__ == '__main__':
    print(Solution().partition("aab"))

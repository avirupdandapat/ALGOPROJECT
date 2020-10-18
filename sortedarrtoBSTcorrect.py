# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : tuple of integers
    # @return the root node in the tree
    def sortedArrayToBST(self, A):
        if len(A) == 0:
            return None
        mid = len(A) // 2
        root = TreeNode(A[mid])
        root.left = self.sortedArrayToBST(A[:mid])
        root.right = self.sortedArrayToBST(A[mid + 1:])
        return root


if __name__ == '__main__':
    A = [1, 2, 3, 4, 5, 6, 7]


    def pr(curr, currleft, currright):
        print('Tree', currleft.val, curr.val, currright.val)
        if currleft.left is not None and currleft.right is not None:
            pr(currleft, currleft.left, currleft.right)
        if currright.left is not None and currright.right is not None:
            pr(currright, currright.left, currright.right)


    result = Solution().sortedArrayToBST(A)
    resultl = result.left
    resultr = result.right
    pr(result, resultl, resultr)

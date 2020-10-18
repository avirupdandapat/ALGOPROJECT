# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return an integer
    def isExactRotate(self, A, B):
        if A is None and B is None:
            return True
        if A is None or B is None:
            return False
        return A.val == B.val and self.isExactRotate(A.left, B.right) and self.isExactRotate(A.right, B.left)

    def isSymmetric(self, A):
        if A is None:
            return 1
        if self.isExactRotate(A.left, A.right):
            return 1
        return 0

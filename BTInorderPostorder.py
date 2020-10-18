# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return the root node in the tree
    def buildTree(self, A, B):
        l = len(A)
        if l == 0:
            return None

        rootVal = B[-1]
        root = TreeNode(rootVal)

        lt = []
        rt = []

        nodeInA = A.index(rootVal)

        lt = B[:nodeInA]
        rt = B[nodeInA:l - 1]

        root.left = self.buildTree(A[:nodeInA], lt)
        root.right = self.buildTree(A[nodeInA + 1:], rt)

        return root

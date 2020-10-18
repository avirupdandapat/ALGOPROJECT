# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def treePathsSumUtil(root, val):
    # Base Case
    if root is None:
        return 0

    # Update val
    val = (val * 10 + root.val)

    # If current node is leaf, return the current value of val
    if root.left is None and root.right is None:
        return val

    # Recur sum of values for left and right subtree
    return (treePathsSumUtil(root.left, val) +
            treePathsSumUtil(root.right, val))


class Solution:
    # @param A : root node of tree
    # @return an integer
    def sumNumbers(self, A):
        return treePathsSumUtil(A, 0) % 1003

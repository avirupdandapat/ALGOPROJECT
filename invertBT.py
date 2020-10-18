# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def invertTree(self, A):
        if A is None:
            return None

        def iterate(n):
            if n.left is not None and n.right is not None:
                left = n.left
                n.left = n.right
                n.right = left
                iterate(n.left)
                iterate(n.right)

        iterate(A)

        return A


if __name__ == '__main__':
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    f = TreeNode(6)
    g = TreeNode(7)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g
    root = Solution().invertTree(a)


    def pr(n):
        if n.left is not None and n.right is not None:
            print(n.left.val, n.val, n.right.val)
            pr(n.left)
            pr(n.right)


    pr(root)

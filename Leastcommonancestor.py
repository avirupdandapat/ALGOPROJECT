# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    def lca(self, A, B, C):
        root = A
        l = B
        r = C
        if not self.check(root, l) or not self.check(root, r):
            return -1
        ans = self.find(root, l, r)
        if ans:
            return ans.val
        return -1

    def check(self, root, val):

        if not root:
            return False
        if root.val == val:
            return True
        if root.left and self.check(root.left, val) or \
                root.right and self.check(root.right, val):
            return True
        return False

    def find(self, root, l, r):
        if not root: return

        if root.val == l or root.val == r:
            return root

        left = self.find(root.left, l, r)
        right = self.find(root.right, l, r)
        if left and right:
            return root

        return left if left else right

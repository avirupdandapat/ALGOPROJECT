# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def dfs(self, root):
        if root is None:
            return 0
        l = self.dfs(root.left)
        r = self.dfs(root.right)
        s0 = max(max(l, r) + root.val, root.val)
        s1 = max(l + r + root.val, s0)
        self.res.append(s1)
        return s0

    def maxPathSum(self, root):
        self.res = []
        self.dfs(root)
        # print(self.res)
        return max(self.res)

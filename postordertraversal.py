# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def postorderTraversal(self, A):
        res = []
        stack = [A]
        while stack:
            pop = stack.pop()
            res.append(pop.val)
            if pop.right:
                stack.append(pop.right)
            if pop.left:
                stack.append(pop.left)


        return res


if __name__ == '__main__':
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(9)
    e = TreeNode(11)
    f = TreeNode(13)
    g = TreeNode(17)
    h = TreeNode(25)
    i = TreeNode(57)
    j = TreeNode(90)
    e.left = b
    e.right = f
    b.left = a
    b.right = d
    d.left = c
    f.right = i
    i.right = j
    i.left = h
    h.left = g

    print(Solution().postorderTraversal(e))

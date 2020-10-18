# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def inorderTraversal(self, A):
        stack = []
        node = A
        res = []
        while len(stack) > 0 or node is not None:

            if node is not None:
                stack.append(node)
                node = node.left
                # stack.push(node)
            else:
                # ans.append(node.val)
                node = stack.pop()
                res.append(node.val)
                node = node.right
        return res


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
    print(Solution().inorderTraversal(a))

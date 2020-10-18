# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def t2Sum(self, A, B):
        if not A:
            return None
        elif A.left is None or A.right is None:
            return 0
        if A.val + A.left.val == B or A.val + A.right.val == B:
            return 1
        self.t2Sum(A.left, B)
        self.t2Sum(A.right, B)

        return 0


if __name__ == '__main__':
    a = TreeNode(10)
    b = TreeNode(9)
    c = TreeNode(20)
    a.left = b
    a.right = c
    print(Solution().t2Sum(a, 30))

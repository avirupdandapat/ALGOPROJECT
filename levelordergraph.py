# Definition for a  binary tree node
from _collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def levelOrder(self, A):
        res = []
        q = deque()
        q.append(A)
        res.append([A.val])
        ls = []
        while q:
            cur = q.popleft()
            ls.append(cur.val)
            q2 = deque()
            while q:
                if cur.left is not None:
                    q2.append(cur.left)
                if cur.right is not None:
                    q2.append(cur.right)
            q = q2
            res.append(ls)


        return res


if __name__ == '__main__':
    a = TreeNode(3)
    b = TreeNode(9)
    c = TreeNode(20)
    d = TreeNode(15)
    e = TreeNode(7)
    a.left = b
    a.right = c
    c.right = e
    c.left = d
    print(Solution().levelOrder(a))

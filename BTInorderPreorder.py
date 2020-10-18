# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


import collections


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return the root node in the tree
    def buildTree(self, A, B):
        def build(stop):
            if not A or B[0] == stop:
                return None

            root = A.popleft()
            node = TreeNode(root)
            node.left = build(root)
            B.popleft()
            node.right = build(stop)

            return node

        A = collections.deque(A)
        B = collections.deque(B)
        return build(None)

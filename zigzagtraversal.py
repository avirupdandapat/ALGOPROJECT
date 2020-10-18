# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def __init__(self):
        self.depth_dict = {}

    def zigzagLevelOrder(self, A):

        def traverse(root, depth):
            if root:
                if depth not in self.depth_dict:
                    self.depth_dict[depth] = []
                traverse(root.left, depth + 1)
                self.depth_dict[depth].append(root.val)
                traverse(root.right, depth + 1)

        traverse(A, 0)
        # print " dict = ",self.depth_dict
        # arr = [self.depth_dict[i] for i in range(len(self.depth_dict))]
        arr = []
        for i in range(len(self.depth_dict)):
            if i & 1:
                self.depth_dict[i] = self.depth_dict[i][::-1]
            arr.append(self.depth_dict[i])
            # print "arr = ",arr
        return arr

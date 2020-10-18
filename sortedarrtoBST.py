# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : tuple of integers
    # @return the root node in the tree
    def sortedArrayToBST(self, A):

        def nodeList(root, Lstart, Lend, Rstart, Rend):
            if Lstart == Lend and Rstart == Rend:
                Lmid = Lstart
                Rmid = Rend
                root.left = TreeNode(A[Lmid])
                root.right = TreeNode(A[Rmid])
            else:
                Lmid = ((Lend + Lstart) // 2)
                Rmid = ((Rend + Rstart) // 2)

                root.left = TreeNode(A[Lmid])
                root.right = TreeNode(A[Rmid])

                nodeList(root.left, Lstart, Lmid, Lmid + 1, Lend)
                nodeList(root.right, Rstart, Rmid, Rmid + 1, Rend)

        rootval = (len(A) // 2)
        mainroot = TreeNode(A[rootval])
        lstart = 0
        lend = rootval - 1
        rstart = rootval + 1
        rend = len(A)-1
        nodeList(mainroot, lstart, lend, rstart, rend)
        return mainroot


if __name__ == '__main__':
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9]


    def pr(curr, currleft, currright):
        print('Tree', currleft.val, curr.val, currright.val)
        if currleft.left is not None and currleft.right is not None:
            pr(currleft, currleft.left, currleft.right)
        if currright.left is not None and currright.right is not None:
            pr(currright, currright.left, currright.right)


    result = Solution().sortedArrayToBST(A)
    resultl = result.left
    resultr = result.right
    pr(result, resultl, resultr)

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : list of integers
    # @return the root node in the tree
    def buildTree(self, A):
        if A is None:
            return A
        root = TreeNode(A[0])
        for i in range(1, len(A)):
            if root.val < A[i]:
                temp = root
                root = TreeNode(A[i])
                root.left = temp
            else:
                temp = TreeNode(A[i])
                currnode = root.left
                while currnode:
                    if temp.val > currnode.val:
                        if currnode.right is not None:
                            currnode = currnode.right
                        else:
                            currnode.right = temp
                            break
                    else:
                        if currnode.left is not None:
                            currnode = currnode.left
                        else:
                            currnode.left = temp
                            break

        return root


if __name__ == '__main__':
    A = [1, 2, 3, 4, 7, 5, 6]
    print(Solution().buildTree(A))
    root = Solution().buildTree(A)


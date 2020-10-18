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
    def pathSum(self, A, B):
        from collections import deque
        stack = deque()
        result = []
        visited = set()
        visited.add(A)
        visited.add(None)
        if not A: return result
        stack.append((A, 0))
        while stack:
            node, ps = stack[-1]
            ps += node.val
            if node.right not in visited:
                visited.add(node.right)
                stack.append((node.right, ps))
            elif node.left not in visited:
                visited.add(node.left)
                stack.append((node.left, ps))
            else:
                if node.left is None and node.right is None \
                        and ps == B:
                    result.append([n[0].val for n in stack])
                stack.pop()

        return result

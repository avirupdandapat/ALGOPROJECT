# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.stack = []
        self.root = root

        cur = root
        while cur is not None:
            self.stack.append(cur)
            cur = cur.left

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return len(self.stack) != 0

    # @return an integer, the next smallest number
    def next(self):
        if self.root is None: return None
        act = self.stack.pop()
        cur = act.right
        while cur is not None:
            self.stack.append(cur)
            cur = cur.left
        return act.val

# Your BSTIterator will be called like this:
# i = BSTIterator(root)
# while i.hasNext(): print i.next(),

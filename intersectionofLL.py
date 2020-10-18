# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def add(self, lisnod):
        self.next = lisnod

    def __str__(self):
        return "{K}\nv={V}".format(
            K=self.next, V=self.val)


class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def getIntersectionNode(self, A, B):
        p1 = A
        p2 = B
        while p1 != p2:
            if p1 is None:
                p1 = B
            else:
                p1 = p1.next
            if p2 is None:
                p2 = A
            else:
                p2 = p2.next
        return p1


if __name__ == '__main__':
    a = ListNode('1')
    a.add(ListNode('2'))
    b = ListNode('3')
    b.add(ListNode('2'))
    print(Solution().getIntersectionNode(a, b))

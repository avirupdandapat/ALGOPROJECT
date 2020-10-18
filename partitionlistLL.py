# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def add(self, lisnod):
        self.next = lisnod


class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def partition(self, A, B):
        curr = A
        l, l1 = [], []
        while curr:
            if curr.val < B:
                l.append(curr.val)
            else:
                l1.append(curr.val)
            curr = curr.next
        l = l + l1
        new = bo = ListNode(None)
        for i in l:
            new.next = ListNode(i)
            new = new.next
        return bo.next


if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(4)
    c = ListNode(3)
    d = ListNode(2)
    e = ListNode(5)
    f = ListNode(2)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    #print(Solution().partition(a, 3))
    res = Solution().partition(a, 3)
    while res:
        print(res.val)
        res = res.next

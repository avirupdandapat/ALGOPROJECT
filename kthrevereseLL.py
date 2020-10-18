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
        # return "v={V}".format(
        # V=self.val)


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reverseList(self, A, B):
        prev = None
        nex = None
        curr = A

        cnt = 0

        while cnt < B:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex

            cnt += 1

        if nex:
            A.next = self.reverseList(nex, B)

        return prev




    def reverse(self, start):
        a = start
        if a.next:
            b = a.next
        else:
            return a
        while b:
            temp = b.next
            b.next = a
            if a == start:
                a.next = None
            a = b
            b = temp
        return a


if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)
    f = ListNode(6)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    print(Solution().reverseList(a, 2))

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def add(self, lisnod):
        self.next = lisnod

    def __str__(self):
        # return "{K}\nv={V}".format(
        # K=self.next, V=self.val)
        return "v={V}".format(
            V=self.val)


def reverseList(A):
    prev = None
    cur = A
    nextptr = None

    while cur:
        nextptr = cur.next
        cur.next = prev
        prev = cur
        cur = nextptr
    return prev


class Solution:
    # @param A : head node of linked list
    # @return an integer

    def lPalin(self, A):
        if A is None:
            return 1
        I = 0
        curr = A
        while curr:
            I += 1
            curr = curr.next
        i = 1
        curr = A
        while i < int(I / 2):
            curr = curr.next
            i += 1

        mid = reverseList(curr.next)
        curr = A
        while mid is not None:
            if curr.val != mid.val:
                return 0
            curr = curr.next
            mid = mid.next
        return 1


if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(0)
    a.next = b
    b.next = c
    print(Solution().lPalin(a))

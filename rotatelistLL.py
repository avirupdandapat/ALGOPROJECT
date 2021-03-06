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
    # @param B : integer
    # @return the head node in the linked list
    def rotateRight(self, A, B):
        dummy = ListNode(None)
        dummy.next = A
        prev = dummy
        curr = A
        for i in range(B):
            if curr is None:
                break
            curr = curr.next
        last = curr
        curr = A
        while last is not None:
            last = last.next
            prev = curr
            curr = curr.next
            print(last.val)
        #prev.next = None
        #last.next = A
        return curr


if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(3)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)
    f = ListNode(6)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    print(Solution().rotateRight(a, 2))

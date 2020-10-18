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
    def reorderList(self, A):
        if not A:
            return A

        mid1, mid2, start2 = self.findmid(A)
        print(mid1.val, mid2.val, start2.val)
        if mid2:
            mid2.next = None
        else:
            mid1.next = None

        if not start2:
            return A

        start2 = self.reverse(start2)

        pointer = A
        while start2:
            temp1 = pointer.next
            pointer.next = start2
            temp2 = start2.next
            start2.next = temp1
            pointer = temp1
            start2 = temp2

        return A

    def findmid(self, A):
        mid1 = A
        pointer = A

        while pointer.next and pointer.next.next:
            pointer = pointer.next.next
            mid1 = mid1.next

        if pointer.next:
            mid2 = mid1.next
            start2 = mid2.next
        else:
            mid2 = None
            start2 = mid1.next

        return mid1, mid2, start2

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
    print(Solution().reorderList(a))

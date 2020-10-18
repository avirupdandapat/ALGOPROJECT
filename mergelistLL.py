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
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, A, B):
        # Add dummy head
        head = ListNode(-1)
        # Set current to head
        curr = head
        while A and B:
            # Add A.val and advance A
            if A.val < B.val:
                curr.next = ListNode(A.val)
                A = A.next
            # Add B.val and advance B
            else:
                curr.next = ListNode(B.val)
                B = B.next
            # Advance current
            curr = curr.next
        # Add remaining A's
        while A:
            curr.next = ListNode(A.val)
            A = A.next
            curr = curr.next
        # Add remaining B's
        while B:
            curr.next = ListNode(B.val)
            B = B.next
            curr = curr.next
        # Remove dummy node
        return head.next


if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(7)
    e = ListNode(8)
    f = ListNode(11)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f

    g = ListNode(4)
    h = ListNode(5)
    i = ListNode(6)
    j = ListNode(9)
    k = ListNode(10)
    l = ListNode(12)
    g.next = h
    h.next = i
    i.next = j
    j.next = k
    k.next = l
    print(Solution().mergeTwoLists(a, g))

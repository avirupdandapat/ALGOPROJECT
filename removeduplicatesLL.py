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
        #return "v={V}".format(
             #V=self.val)


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        dummy = ListNode(0)
        dummy.next = A
        tail = dummy
        while A:
            curr = A
            while A.next and curr.val == A.next.val:
                A = A.next
            if curr == A:
                tail = tail.next
            else:
                tail.next = A.next
            A = A.next
        return dummy.next


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
    print(Solution().deleteDuplicates(a))

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
        if A is None:
            return 1
        elif A.next is None:
            return 1
        cur = A
        cn = 1
        while cur.next:
            if cur.val == cur.next.val:
                if cur.next.next is not None:
                    cur.next = cur.next.next
                else:
                    cur.next = None
            else:
                cur = cur.next
                cn += 1

        return A


if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(3)
    c = ListNode(3)
    d = ListNode(3)
    a.next = b
    b.next = c
    c.next = d
    print(Solution().deleteDuplicates(a))

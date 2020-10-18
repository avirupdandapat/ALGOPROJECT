# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def add(self, lisnod):
        self.next = lisnod


    #def __str__(self):
        #return "{K}\nv={V}".format(
           #K=self.next, V=self.val)
        #return "v={V}".format(
             #V=self.val)


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reverseList(self, A):
        prev = None
        cur = A
        nextptr = None

        while cur:
            nextptr = cur.next
            cur.next = prev
            prev = cur
            cur = nextptr
        return prev


if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    a.next = b
    b.next = c
    print(Solution().reverseList(a))

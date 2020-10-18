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
    # @param B : integer
    # @return the head node in the linked list
    def removeNthFromEnd(self, A, B):
        dummy = ListNode(None)
        dummy.next = A
        prev = dummy
        curr = A
        for i in range(B):
            if curr == None:
                break
            curr = curr.next
        last = curr
        curr = A
        while last != None:
            last = last.next
            prev = curr
            curr = curr.next
        prev.next = curr.next
        return dummy.next

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
    def detectCycle(self, A):

        if not A: return None
        slow = fast = A
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: break

        if slow != fast: return None
        slow = A
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow


if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(1)
    e = ListNode(2)
    f = ListNode(3)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    print(Solution().detectCycle(a))


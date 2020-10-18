# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def add(self, lisnod):
        self.next = lisnod


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def insertionSortList(self, A):
        res = []
        head = A
        while A is not None:
            res.append(A.val)
            A = A.next

        A = head
        res.sort()
        for i in res:
            A.val = i
            A = A.next
        return head


if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(4)
    c = ListNode(3)
    d = ListNode(2)
    e = ListNode(5)
    f = ListNode(2)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    #print(Solution().partition(a, 3))
    res = Solution().insertionSortList(a)
    while res:
        print(res.val)
        res = res.next

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def add(self, lisnod):
        self.next = lisnod




class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        if not A or not B:
            return A or B

        res = A

        carry = 0
        while A and B:
            new_value = A.val + B.val + carry
            A.val = int(new_value % 10)
            carry = int(new_value / 10)

            if not A.next and not B.next:
                break

            if not A.next:
                A.next = ListNode(0)

            if not B.next:
                B.next = ListNode(0)

            A = A.next
            B = B.next

        if carry > 0:
            print(carry)
            A.next = ListNode(carry)

        return res


if __name__ == '__main__':
    a = ListNode(2)
    b = ListNode(4)
    c = ListNode(3)
    d = ListNode(5)
    e = ListNode(6)
    f = ListNode(4)
    a.next = b
    b.next = c
    #c.next = d
    d.next = e
    e.next = f
    #print(Solution().addTwoNumbers(a, d))
    r = Solution().addTwoNumbers(a, d)
    while r:
        print(r.val)
        r = r.next

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
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, A):
        import heapq
        l = []
        for i in range(len(A)):
            l.append([A[i].val, A[i]])

        heapq.heapify(l)
        int_max = 2147483647
        head = ListNode(None)
        curr = head
        while l[0][0] != int_max:
            print('l', l)
            top = heapq.heappop(l)
            temp = top[1]
            print('temp',temp)

            if temp.next is not None:
                heapq.heappush(l, [temp.next.val, temp.next])
            else:
                heapq.heappush(l, [int_max, 0])
            curr.next = temp
            curr = temp
        return head.next


if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(10)
    c = ListNode(20)

    a.next = b
    b.next = c

    d = ListNode(4)
    e = ListNode(11)
    f = ListNode(13)
    d.next = e
    e.next = f

    g = ListNode(3)
    h = ListNode(8)
    i = ListNode(9)
    g.next = h
    h.next = i

    A = [a, d, g]
    print(Solution().mergeKLists(A))
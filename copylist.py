# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def add(self, lisnod):
        self.next = lisnod


class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        head2 = None
        cursor2 = None

        nodeMap = {}
        cursor = head
        while cursor is not None:
            node = RandomListNode(cursor.label)
            if cursor2 is None:
                head2 = node
            else:
                cursor2.next = node
            cursor2 = node
            nodeMap.setdefault(cursor, cursor2)
            cursor = cursor.next

        cursor = head
        while cursor is not None:
            if cursor.random is not None:
                node2 = nodeMap[cursor]
                node2.random = nodeMap[cursor.random]
            cursor = cursor.next

        return head2


if __name__ == '__main__':
    a = RandomListNode(1)
    b = RandomListNode(2)
    c = RandomListNode(3)
    #d = ListNode(5)
    #e = ListNode(6)
    #f = ListNode(4)
    a.next = b
    b.next = c
    # c.next = d
    #d.next = e
    #e.next = f
    # print(Solution().addTwoNumbers(a, d))
    r = Solution().copyRandomList(a)
    while r:
        print(r.label)
        r = r.next

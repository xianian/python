# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        prenode = head
        curnode = head
        while curnode:
            if curnode.val == val:
                if curnode != head:
                    prenode.next = curnode.next
                else:
                    prenode = curnode.next
                    head = prenode
            else:
                if prenode != curnode:
                    prenode = curnode
            curnode = curnode.next
        return head

sol = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(6)
head.next.next.next = ListNode(6)
head.next.next.next.next = ListNode(6)
head.next.next.next.next .next = ListNode(6)
result = sol.removeElements(head,3)
while result:
    print result.val
    result = result.next

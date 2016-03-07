# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        curnode = head
        res = False
        B = {}
        while curnode:
            if curnode not in B:
                B[curnode] = 1
            else:
                B[curnode] = B[curnode] + 1
                if B[curnode] == 2:
                    res = True
                    break
            curnode = curnode.next
        return res

sol = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = head
print sol.hasCycle(head)


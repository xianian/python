# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        prenode = head
        nextnode  = head.next
        while nextnode:
            if prenode.val == nextnode.val:
                prenode.next = nextnode.next
                nextnode = nextnode.next
            else:
                prenode = nextnode
                nextnode = nextnode.next
        return head

sol = Solution()
head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
result = sol.deleteDuplicates(head)
while result:
    print result.val
    result = result.next


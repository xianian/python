# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        reverhead = None
        while head:
            tmpNode = ListNode(head.val)
            tmpNode.next = reverhead
            reverhead = tmpNode
            head = head.next
        return reverhead

sol = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
result = sol.reverseList(head)
while result:
    print result.val
    result = result.next

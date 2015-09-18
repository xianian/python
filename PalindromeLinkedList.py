# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return True
        fast = head
        slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        reverhalf = None
        curnode = slow.next
        while curnode:
            tmpnode =curnode.next
            curnode.next = reverhalf
            reverhalf = curnode
            curnode = tmpnode
        ret = True
        p1 =reverhalf
        p2 = head
        while p1:
            if p1.val != p2.val:
                ret = False
                break
            p1 = p1.next
            p2 = p2.next
        return ret

sol = Solution()
head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(1)
print sol.isPalindrome(head)

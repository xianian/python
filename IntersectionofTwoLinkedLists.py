# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        C = {}
        res = None
        tmpA = headA
        tmpB = headB
        while tmpA:
            if tmpA not in C:
                C[tmpA] = 1
            else:
                print "input error"
            tmpA = tmpA.next
        while tmpB:
            if tmpB not in C:
                C[tmpB] = 1
            else:
                res = tmpB
                break
            tmpB = tmpB.next
        return res

sol = Solution()
l1 = ListNode(1)
l1.next = ListNode(2)
l2 = ListNode(3)
l2.next = ListNode(4)
l3 = ListNode(5)
l3.next = ListNode(6)
l1.next.next = l3
l2.next.next = l3
res = sol.getIntersectionNode(l1,l2)
while res:
    print res.val
    res = res.next



# Definition for binary tree with next pointer.
import Queue
class TreeLinkNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if root:
            levelqueue = Queue.Queue()
            nextlevelqueue = Queue.Queue()
            nextlevelqueue.put(root)
            while True:
                if levelqueue.empty():
                    if not nextlevelqueue.empty():
                        prenode = None
                        while not nextlevelqueue.empty():
                            levelqueue.put(nextlevelqueue.get())
                    else:
                        break
                curnode = levelqueue.get()
                if levelqueue.empty():
                    if prenode:
                        #print prenode.val
                        #print curnode.val
                        prenode.next  = curnode
                    #print curnode.val
                    curnode.next = None
                else:
                    if prenode:
                        #print prenode.val
                        #print curnode.val
                        prenode.next = curnode
                if curnode.left:
                    nextlevelqueue.put(curnode.left)
                if curnode.right:
                    nextlevelqueue.put(curnode.right)
                prenode = curnode

sol = Solution()
root = TreeLinkNode(1)
root.left = TreeLinkNode(2)
root.right = TreeLinkNode(3)
#root.left.left = TreeLinkNode(4)
root.left.right = TreeLinkNode(5)
#root.right.left = TreeLinkNode(6)
root.right.right = TreeLinkNode(7)

sol.connect([])

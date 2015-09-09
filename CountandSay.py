class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        strlist = "1"
        while(n):
        	if n == 1: 
        		break
        	else:
        		tmp = ""
        		count = 0
        		for i in range(len(strlist)):
        			if i == 0 or strlist[i] == strlist[i - 1]:
        				count = count + 1
        			else:
        				tmp = tmp + str(count)
        				tmp = tmp + strlist[i - 1]
        				count = 1
        		if count != 0:
        			tmp = tmp + str(count)
        			tmp = tmp + strlist[i] 
        			count = 0
        		strlist = tmp
        		n = n - 1
        return strlist

sol = Solution()
print sol.countAndSay() 
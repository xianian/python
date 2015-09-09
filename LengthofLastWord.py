class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        strlist = s.split(' ')
        lenstrlist = len(strlist)
        for i in range(lenstrlist):
        	if len(strlist[lenstrlist - 1 -i]) != 0:
        		return  len(strlist[lenstrlist - 1 -i])

sol = Solution()
print sol.lengthOfLastWord("hello  dssh         sadjhsad")
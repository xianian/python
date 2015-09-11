import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        p = re.compile("[^\d^\w]")
        ps = p.sub('',s)
        reverps =ps[::-1]
        if ps.upper() == reverps.upper():
            return True
        else:
            return False

sol = Solution()
print sol.isPalindrome("race a car")

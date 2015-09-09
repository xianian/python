class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(str(int(a,2) + int(b,2))))[2:]

sol = Solution()
print sol.addBinary("1","11")

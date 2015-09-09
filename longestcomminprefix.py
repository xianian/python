__author__ = 'Thinkpad'
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        lenlist = len(strs)
        commonprefix = ""
        j = 0
        while True:
            curchar = ""
            for i in range(lenlist):
                if j >= len(strs[i]):
                    curchar = ""
                    break
                if i == 0:
                    curchar = strs[i][j]
                else:
                    if curchar != strs[i][j]:
                        curchar = ""
                        break
            if curchar != "":
                commonprefix = commonprefix + curchar
                j = j + 1
            else:
                break
        return commonprefix

sol = Solution()
strs = []
print sol.longestCommonPrefix(strs)
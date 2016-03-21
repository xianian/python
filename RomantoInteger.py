class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romandict = {'I':1,'X':10,'C':100,'M':1000,'V':5,'L':50,'D':500}
        s.upper();
        ret = 0
        lastc = 0
        for c in s:
            if lastc == 0:
                lastc = romandict[c]
            else:
                if lastc < romandict[c]:
                    ret -= lastc
                else:
                    ret += lastc
                lastc = romandict[c]
        ret += lastc
        return ret

if __name__ == "__main__":
    Sol = Solution()
    print Sol.romanToInt("MMMCMICD")

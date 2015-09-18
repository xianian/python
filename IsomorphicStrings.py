class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dicts = {}
        dictt = {}
        lens = len(s)
        lent = len(t)
        ret = True
        if lens != lent:
            ret = False
        else:
            for i in range(lens):
                if s[i] not in dicts:
                    dicts[s[i]] = t[i]
                else:
                    if dicts[s[i]] != t[i]:
                        ret = False
                        break
            if ret == True:
                for i in range(lent):
                    if t[i] not in dictt:
                        dictt[t[i]] = s[i]
                    else:
                        if dictt[t[i]] != s[i]:
                            ret = False
                            break
        return ret

sol = Solution()
print sol.isIsomorphic("eb","aa")

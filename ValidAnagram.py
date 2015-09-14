class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = "".join((lambda x:(x.sort(),x)[1])(list(s)))
        t = "".join((lambda x:(x.sort(),x)[1])(list(t)))
        if s == t:
            return True
        else:
            return False

sol = Solution()
print sol.isAnagram("anagram","nagaram")

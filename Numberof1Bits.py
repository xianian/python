class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            count = count + (n & 1)
            n = n >> 1
        return count

sol = Solution()
print sol.hammingWeight(15)

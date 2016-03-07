class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        if len(prices) > 0:
            minv = prices[0]
        for v in prices:
            if v - minv > profit:
                profit = v - minv
            if minv > v:
                minv = v
        return profit

sol = Solution()
print sol.maxProfit([])

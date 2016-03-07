class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        minindex = 0
        lenprices = len(prices)
        for i in range(1,lenprices):
            if prices[i] > prices[i - 1]:
                profit = profit + prices[i] - prices[i - 1]
        return profit
sol = Solution()
print sol.maxProfit([1,4,2,5,2,1,0])

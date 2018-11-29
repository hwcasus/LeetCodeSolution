# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        current_low = None
        profit = 0
        for i in range(len(prices)):
            if current_low is None or current_low > prices[i]:
                current_low = prices[i]
            else:
                profit = max(prices[i] - current_low, profit)
    
        return profit
    
     def maxProfitOld(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = sys.maxsize
        profit = 0
        
        for p in prices:
            if p < min_price:
                min_price = p
            else:
                diff = p - min_price
                if diff > profit:
                    profit = diff
                    
        return profit
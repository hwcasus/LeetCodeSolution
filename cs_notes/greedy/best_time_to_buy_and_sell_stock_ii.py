# 122. Best Time to Buy and Sell Stock II
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        
        profit = 0
        for i in range(len(prices[:-1])):
            if prices[i] < prices[i+1]:
                profit += prices[i+1] - prices[i]
        
        return profit 
    
    def maxProfitOld(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        have_bought = False
        buy_in_price = prices[0]
        profit = 0
        
        for price in prices[1:]:
            tmp = price - buy_in_price
            if tmp > 0:
                profit += tmp
        
            buy_in_price = price
            
            
        return profit
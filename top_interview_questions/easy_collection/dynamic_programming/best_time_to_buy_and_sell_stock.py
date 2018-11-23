# Best Time to Buy and Sell Stock
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/572/

class Solution:
    def maxProfit(self, prices):
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
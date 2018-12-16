# 322. Coin Change
# https://leetcode.com/problems/coin-change/description/

class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        本題想法很簡單, 從 1 塊錢 -> amount 塊錢來算最少要花多少硬幣
        先假設 amount = 11, 錢幣種類有 [1, 2, 5]
        所以可以知道, 若要將 11 塊往下分, 一定只有
        1) 5 塊硬幣 + 剩下 7 塊
        2) 2 塊硬幣 + 剩下 9 塊
        3) 1 塊硬幣 + 剩下 10 塊
        也就是說我們必須只要知道 7, 9, 10 塊最少只需要多少枚硬幣, 就可以知道答案
        但這三者分別也都可以往下拓展, 所以我們要從一塊錢開始往上推
        首先 dp 長度為 11+1, dp[0]設0, 對所有錢的大小我們都去檢查, 舉例來說
        1 塊錢 : 1 枚 1 塊 -> dp[1] = 1, 2塊錢跟5塊錢太大了
        2 塊錢 : 
            1 枚 1 塊 + 剩下 1 塊錢 -> dp[1] + 1 = 2 枚
            1 枚 2 塊 -> 1 枚
            1 枚 5 塊太大了
            所以得出 dp[2] = min(dp[1]+1, dp[2]) 也就是 1 枚
        所以規則會是
        對 1-n 塊錢, 都去檢查用所有貨幣扣掉之後最少要多少枚, 這樣就會知道當前的錢最少可以用多少枚
        然後不斷往上更新直到 n 就可以回傳 dp[n]
        """
        
        MAX = amount+1
        dp = [0] + [MAX for _ in range(amount)]
        
        for i in range(1, amount+1):
            dp[i] =  min([dp[i-coin] if i >= coin else MAX for coin in coins]) + 1
            
            # print(dp)
        
        return dp[-1] if dp[-1] <= amount else -1
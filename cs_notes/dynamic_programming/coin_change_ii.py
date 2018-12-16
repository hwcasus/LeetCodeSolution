# 518. Coin Change 2
# https://leetcode.com/problems/coin-change-2/description/

class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        本題和 Coin Change 是類似題, 不同的是本次不問最少枚數
        而是要求你算出總共有幾種不同的組法
        這邊要求不同就隱含著順序的問題
        也就是 '2+1+1' 跟 '1+2+1' 跟 '1+1+2' 是一樣的組法
        因此在雙迴圈的順序是有非常重要的, 必須是先根據錢種來迴圈
        如果先根據金額量來迴圈, 就會發生上面提到的重複問題
        舉例來說, 目標金額是 3, 金幣只有 [1, 2]
        所以應該只有3種方法 [1, 1, 1, 1], [1, 1, 2], [2, 2]
        但如果先從金額開始算(以下公式使用 dp[i] += dp[i-coin])
            dp[1] = 1 [1]
            dp[2] = 2 [1, 1], [2]
            dp[3] = 3 [1, 2], [1, 1, 1], [2, 1]
        可以看到 [1, 2] 和 [2, 1] 就會重複, 但如果先根據錢種的話
            Coin = 1
                dp[1] = 1, [1]
                dp[2] = 1, [1, 1]
                dp[3] = 1, [1, 1, 1]
            Coin = 2
                dp[1] = 1 + 0
                dp[2] = 1 + 1, [2]
                dp[3] = 1 + 1, [2, 1]
        所以順序非常重要, 其目的在於避免混亂的錢幣大小順序影響計算數量
        """
        dp = [1] + [0] * (amount)
        for coin in coins:
            for i in range(1, amount+1):
                if i >= coin:
                    dp[i] += dp[i-coin]
            # print (dp)
        return dp[-1]
    
    def changeDFS(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        if not amount: return 1
        if not coins: return 0
        
        stack = []
        self.ret=0
        coins.sort(reverse=True)
        def go(current_amount):
            if current_amount == 0:
                self.ret += 1
            if current_amount < coins[-1]: return 
            for i, coin in enumerate(coins):
                if stack and stack[-1] < coin: continue
                if current_amount >= coin:
                    stack.append(coin)
                    go(current_amount-coin)
                    stack.pop()
        go(amount)
        return self.ret
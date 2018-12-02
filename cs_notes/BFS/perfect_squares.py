# 279. Perfect Squares
# https://leetcode.com/problems/perfect-squares/description/

class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [i for i in range(n+1)] # 最糟的情況就是全部都用 1**2 加起來
        squares = [i**2 for i in range(1, int(n**0.5)+1)]
        for i in range(1, n+1):
            for s in squares:
                if i < s: break
                dp[i] = min(dp[i], dp[i-s]+1) # 比較看看全用 1 或是上一個加起來的看誰比較小
            
        return dp[-1]
        
    def numSquaresBFS(self, n):
        """
        :type n: int
        :rtype: int
        """
        visited = [False]*(n+1)
        queue = [n]
        squares = {i:i**2 for i in range(1, int(n**0.5)+1)}
        
        step = 0
        while queue:
            step +=1
            for i in range(len(queue)):
                curr = queue.pop(0)
                for _, s in squares.items():
                    nxt = curr - s;
                    if nxt < 0: break
                    if nxt == 0: return step
                    if visited[nxt]:continue
                    
                    visited[nxt] = True;
                    queue.append(nxt);
            
        return n
            

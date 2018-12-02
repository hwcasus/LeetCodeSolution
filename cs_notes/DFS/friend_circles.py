# 547. Friend Circles
# https://leetcode.com/problems/friend-circles/description/

class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        
        row = len(M)
        visited = [False]*row
        
        def go(c):
            visited[c]=True
            for other in range(row):
                if M[c][other] == 1 and not visited[other]:
                    go(other)
    
        count = 0
        for i in range(row):
            if not visited[i]:
                count+=1
                go(i)
                
        return count

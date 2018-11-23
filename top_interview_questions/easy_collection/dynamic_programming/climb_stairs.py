# Climbing Stairs
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/569/

class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return n
        
        prev_1 = 1
        prev_2 = 2
        curr = 0
        
        while n >= 3:
            curr = prev_1 + prev_2
            prev_1 = prev_2
            prev_2 = curr
            n -= 1
        
        return curr
    
    def climbStairsFailed(self, n):
        if n < 3:
            return n
        else:
            return self.climbStairsFailed(n-2) + self.climbStairsFailed(n-1)
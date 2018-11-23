# House Robber
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/576/

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        pre1 = 0
        pre2 = 0
        curr = 0
        
        for n in nums:
            curr = max(pre1, pre2 + n)
            pre2 = pre1
            pre1 = curr
            
        return curr
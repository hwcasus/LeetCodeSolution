# 77. Combinations
# https://leetcode.com/problems/combinations/description/

class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        
        ret = []
        def go(current, idx):
            if len(current) == k:
                ret.append(current)
                return
            
            for i in range(idx, n+1):
                go(current+[i], i+1)
        
        go([], 1)
        return ret
    

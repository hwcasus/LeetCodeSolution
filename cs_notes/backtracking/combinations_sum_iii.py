# 216. Combination Sum III
# https://leetcode.com/problems/combination-sum-iii/description/

class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        
        ret = []
        
        def go(current, idx):
            if sum(current) > n or len(current) > k : return
            if sum(current) == n and len(current) == k:
                # print(sum(current), len(current), 'ya')
                ret.append(current)
                return
            # print(sum(current), len(current))
            for i in range(idx, 10):
                go(current+[i], i+1)
        
        go([], 1)
        return ret
                
            
            
            

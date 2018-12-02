# 39. Combination Sum
# https://leetcode.com/problems/combination-sum/description/

class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        ret = []
        def go(current, idx):
            if sum(current) > target: return 
            if sum(current) == target:
                ret.append(current)
                return
            
            for i in range(idx, len(candidates)):
                go(current+[candidates[i]], i)
        
        go([], 0)
        return ret

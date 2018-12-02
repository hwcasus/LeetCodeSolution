# 40. Combination Sum II
# https://leetcode.com/problems/combination-sum-ii/description/

class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        ret = []
        candidates.sort()
        def go(current, candidates):
            if sum(current) > target: return
            if sum(current) == target:
                ret.append(current) 
                return
            
            for i in range(len(candidates)):
                if i>0 and candidates[i] == candidates[i-1]: continue # 同一層的話, 跟上一個同樣就跳過, 
                rest_candidates = candidates[i+1:] # 只往後找, 因排序過所以只會找到一樣大或是更大的
                go(current+[candidates[i]], rest_candidates)
        
        go([], candidates)
        # print(ret)
        return ret

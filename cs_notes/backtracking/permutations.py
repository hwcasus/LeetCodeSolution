# 46. Permutations
# https://leetcode.com/problems/permutations/description/

class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        ret = []
        
        def go(current):
            if len(current) == len(nums):
                if current not in ret: ret.append(current)
                return
            for i, n in enumerate(nums):
                if n not in current: go(current+[n])
        
        go([])
        return ret
    
    def permuteClever(self, nums):
        """ Use a boolean list to record current path.
        and reset the bool value after pop
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.visited = [False] * len(nums)
        results = []
        tmp = []
        step = 0
        
        self.helper(results, tmp, nums, step)
        
        return results
    
    def helper(self, results, tmp, nums, step):
        
        if step == len(nums):
            results.append(tmp[:])
            return
        
        for i, num in enumerate(nums):
            if not self.visited[i]:
                tmp.append(num)
                self.visited[i] = True
                self.helper(results, tmp, nums, step + 1)
                tmp.pop()
                self.visited[i] = False
                
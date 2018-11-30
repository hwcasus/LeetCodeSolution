# 78. Subsets
# https://leetcode.com/problems/subsets/description/

class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        ret = []
        
        for i in range(2**len(nums)):
            if_take = [int(c) for c in bin(i)[2:]]
            if_take = [0]*(len(nums)-len(if_take)) + if_take 
            ret.append([nums[i] for i, b in enumerate(if_take) if bool(b)])
        
        return ret
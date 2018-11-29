# 169. Majority Element
# https://leetcode.com/problems/majority-element/description/

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        return sorted(nums)[(len(nums)//2)]
        
    def majorityElementSlow(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        d = {}
        for n in nums:
            d.setdefault(n, 0)
            d[n] += 1
            if d[n] > (len(nums)//2): return n
            
        return -1
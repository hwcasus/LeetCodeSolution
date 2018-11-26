# 136. Single Number
# https://leetcode.com/problems/single-number/description/

class Solution:
    def singleNumber(self, nums):
        ret = 0
        for n in nums:
            ret ^= n
        return ret
        
    def singleNumberOld(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) == 1:
            return nums[0]
        
        dist_nums = list(set(nums))
        
        sums = 0
        
        for n in nums:
            sums+=n
        for n in dist_nums:
            sums-=n
        for n in dist_nums:
            sums-=n
        
        return sums*-1
            
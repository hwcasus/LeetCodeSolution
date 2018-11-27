# 283. Move Zeroes
# https://leetcode.com/problems/move-zeroes/description/

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        idx = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[idx], nums[i] = nums[i], nums[idx]
                idx += 1
        
                
        
    def moveZeroesOld(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zeros = []
        
        while 0 in nums:
            nums.remove(0)
            zeros += [0]
            
        nums += zeros
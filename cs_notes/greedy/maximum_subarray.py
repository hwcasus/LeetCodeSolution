# 53. Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/description/

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        pre_sum, current_sum = 0, 0
        for i in range(0, len(nums)):
            
            if nums[i] + pre_sum > 0:
                pre_sum += nums[i]
            else:
                pre_sum = 0
                
            current_sum = max(current_sum, pre_sum)
        return current_sum
            
    def maxSubArraySoCool(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        
        return max(nums)
    
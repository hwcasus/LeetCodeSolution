# 665. Non-decreasing Array
# https://leetcode.com/problems/non-decreasing-array/description/

class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        c = 0
        nums_length = len(nums)
        
        for i in range(1, nums_length):
            if c >= 2:
                return False
            if nums[i-1] <= nums[i]:
                continue
            
            c += 1
            if i >= 2 and nums[i-2] > nums[i]:
                nums[i] = nums[i-1]
            else:
                nums[i-1] = nums[i]
                    
        return True if c < 2 else False
                    
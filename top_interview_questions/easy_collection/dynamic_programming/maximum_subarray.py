# Maximum Subarray
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/566/

class Solution:
    def maxSubArraySlow(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums or len(nums) == 0:
            return 0
        
        max_so_far, max_at_here = nums[0], nums[0]
        for n in nums[1:]:
            max_at_here = max(0, max_at_here) + n
            max_so_far = max(max_so_far, max_at_here)
        
        return max_so_far
    def maxSubArrayA(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        max_at_here = nums[0]
        max_so_far = [max_at_here]
        for i in range(1, len(nums)):
            if max_at_here < 0:
                max_at_here = nums[i]
            else:
                max_at_here += nums[i]
            max_so_far.append(max_at_here)
    
        return max(max_so_far)
    
    def maxSubArrayB(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        
        return max(nums)
    
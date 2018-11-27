# 503. Next Greater Element II
# https://leetcode.com/problems/next-greater-element-ii/description/

class Solution:
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        len_nums = len(nums)
        ans = [-1] * len_nums
        stack = []
        
        for i, n in enumerate(nums+nums):
            while stack and nums[stack[-1]] < n:
                ans[stack.pop()] = n
            stack.append(i%len_nums)
        return ans
        
    
    def nextGreaterElementsWhyButFaster(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [-1]*len(nums) 
        stack = []
        
        for i, n in enumerate(nums):
            while stack and nums[stack[-1]] < n:
                ans[stack.pop()] = n
            stack.append(i)
        
        for i, n in enumerate(nums):
            while stack and nums[stack[-1]] < n:
                ans[stack.pop()] = n
            stack.append(i)
        
        return ans
        
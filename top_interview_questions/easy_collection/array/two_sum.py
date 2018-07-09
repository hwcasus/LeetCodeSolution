"""
Two Sum

https://leetcode.com/problems/two-sum/

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].
"""

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        search_mode = False
        ans = []
        res = 0
        
        for i, n in enumerate(nums):
            if not search_mode:
                if target - n in nums[i+1:]:
                    ans += [i]
                    search_mode = True
                    res = target - n
            else:
                if n == res:
                    ans += [i]
                    
        
        return ans
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
        
        d = {}
        for i, n in enumerate(nums):
            l = target - n
            # 如果字典中沒有正在找的餘數這個 key, 那就把自己跟idx 寫入字典
            # 因為題目保證有一對, 所以一定有另外一個數字會需要找到自己跟自己的idx
            if l in d: return [d[l], i]
            else:d[n] = i


    def twoSumOld(self, nums, target):
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
